import platform
from collections.abc import Callable
from datetime import datetime
from enum import StrEnum
from typing import Any, cast

import httpx
from anthropic import (
    Anthropic,
    AnthropicBedrock,
    AnthropicVertex,
    APIError,
    APIResponseValidationError,
    APIStatusError,
)
from anthropic.types.beta import (
    BetaCacheControlEphemeralParam,
    BetaContentBlockParam,
    BetaImageBlockParam,
    BetaMessage,
    BetaMessageParam,
    BetaTextBlock,
    BetaTextBlockParam,
    BetaToolResultBlockParam,
    BetaToolUseBlockParam,
)

from .tools import BashTool, ComputerTool, EditTool, ToolCollection, ToolResult

COMPUTER_USE_BETA_FLAG = "computer-use-2024-10-22"
PROMPT_CACHING_BETA_FLAG = "prompt-caching-2024-07-31"


class APIProvider(StrEnum):
    ANTHROPIC = "anthropic"
    BEDROCK = "bedrock"
    VERTEX = "vertex"


PROVIDER_TO_DEFAULT_MODEL_NAME: dict[APIProvider, str] = {
    APIProvider.ANTHROPIC: "claude-3-5-sonnet-20241022",
    APIProvider.BEDROCK: "anthropic.claude-3-5-sonnet-20241022-v2:0",
    APIProvider.VERTEX: "claude-3-5-sonnet-v2@20241022",
}


# This system prompt is optimized for the Docker environment in this repository and
# specific tool combinations enabled.
# We encourage modifying this system prompt to ensure the model has context for the
# environment it is running in, and to provide any additional information that may be
# helpful for the task at hand.
# Define your SYSTEM_PROMPT with proper triple quotes
SYSTEM_PROMPT = """
<SYSTEM_CAPABILITY>
Commands to launch pre-installed applications:

**Firefox Browser**:
1. DISPLAY=:1 && gtk-launch firefox-esr
2. DISPLAY=:1 firefox-esr &
3. Kill: pkill -f firefox-esr

**Text Editor (Gedit)**:
1. Launch: DISPLAY=:1 gedit &
2. Alternative: DISPLAY=:1 /usr/bin/gedit &
3. Alternative: gtk-launch org.gnome.gedit &
4. Kill: pkill gedit

**Terminal**:
1. Launch: DISPLAY=:1 xterm &
2. Alternative: DISPLAY=:1 /usr/bin/xterm &
3. Alternative: x-terminal-emulator &
4. Kill: pkill xterm

**Calculator**:
1. Launch: DISPLAY=:1 galculator &
2. Alternative: DISPLAY=:1 /usr/bin/galculator &
3. Alternative: gtk-launch galculator &
4. Kill: pkill galculator

**Paint**:
1. Launch: DISPLAY=:1 xpaint &
2. Alternative: DISPLAY=:1 /usr/bin/xpaint &
3. Alternative: (cd /tmp && DISPLAY=:1 xpaint) &
4. Kill: pkill xpaint

**PDF Viewer**:
1. Launch: DISPLAY=:1 xpdf &
2. Alternative: DISPLAY=:1 /usr/bin/xpdf &
3. Alternative: evince &
4. Kill: pkill xpdf

**Spreadsheet**:
1. Launch: DISPLAY=:1 libreoffice --calc &
2. Alternative: DISPLAY=:1 /usr/bin/libreoffice --calc &
3. Alternative: soffice --calc &
4. Kill: pkill -f libreoffice

**For new applications**:
1. Check availability: which app_name
2. Install if needed: sudo apt update && sudo apt install -y app_name
3. Launch: DISPLAY=:1 app_name &
4. Kill if running: pkill -f app_name

Note: If an application fails to launch:
1. Check if already running: ps aux | grep app_name
2. Kill existing process if needed: pkill -f app_name
3. Try alternate launch command if available

**System Details & Usage Tips**:  
- Ubuntu VM ({platform.machine()} architecture) with internet access.  
- Use `curl` instead of `wget`.  
- Set `export DISPLAY=:1` before launching GUI apps.  
- GUI apps take time to load; confirm with screenshots.  
- When using bash commands that produce large outputs, display them directly in the console without redirecting to files.  
- When viewing a page, zoom out or scroll down before deciding content isn't available.  
- Function calls may take time to execute; chain multiple calls into a single request when possible.  
- Chain multiple bash calls to save time.  
Date: {datetime.today().strftime('%A, %B %-d, %Y')}.  
</SYSTEM_CAPABILITY>

<IMPORTANT_BROWSER_INTERACTION>
* When analyzing a website, ALWAYS perform these steps in the given order:
  1. Take an initial screenshot of the page.
  2. Inspect the HTML structure using browser developer tools and network tools wherever necessary.
  3. Verify all selectors using multiple methods.
  4. Document the selector verification results.
  5. Test dynamic behaviors and AJAX interactions.
</IMPORTANT_BROWSER_INTERACTION>

<SELECTOR_VERIFICATION_PROTOCOL>
1. **Initial Analysis**:
   - Take a screenshot of the target page.
   - Inspect the HTML structure to understand the layout.
   - Identify and note static elements.
   - Identify and note dynamic elements.

2. **Selector Verification Process** (Mandatory for EACH element):
   a) **Primary Verification**:
      ```javascript
      // Browser Console Commands
      // 1. ID verification
      document.getElementById('elementId');

      // 2. Name verification
      document.getElementsByName('elementName');

      // 3. CSS verification
      $$('selector');

      // 4. XPath verification
      $x("//xpath");
      ```

   b) **Secondary Verification**:
      - Manual inspection using the HTML structure.
      - Selenium IDE recording to test interactions.
      - Chrome DevTools "Elements" panel for confirmation.

3. **Selector Priority & Documentation**:
   For each element, prioritize selectors in this order:
   - ID
   - Name
   - CSS
   - XPath

   Document the following for each selector:
   - Primary selector (highest priority available).
   - Alternative selectors (at least two alternatives).
   - Verification methods used.
   - Stability assessment.
   - Dynamic state handling results.

4. **Dynamic State Verification**:
   - Analyze AJAX interactions using the Network tab.
   - Document state changes and behaviors.
   - Record load time behavior and event triggers.

5. **Cross-browser Verification**:
   - Test the selectors in Firefox.
   - Test the selectors in Chrome (or other available browsers).
</SELECTOR_VERIFICATION_PROTOCOL>

<SELECTOR_DOCUMENTATION_TEMPLATE>
For each element, provide the following details:

Element: [Element Name]  
Primary Selector:  
- Type: [ID/Name/CSS/XPath]  
- Value: [Selector value]  
- Verification Method 1: [Console command + result]  
- Verification Method 2: [Alternative method + result]  

Alternative Selectors:  
1. Type: [Selector type]  
   Value: [Selector value]  
   Verification: [Method + result]  
2. Type: [Selector type]  
   Value: [Selector value]  
   Verification: [Method + result]  

Dynamic Behavior:  
- AJAX Interactions: [Yes/No]  
- State Changes: [Details of changes]  
- Load Behavior: [Details of load events]  
</SELECTOR_DOCUMENTATION_TEMPLATE>

<CODE_GENERATION_RULES>
No selector should be included in the code without:
1. Two verified methods of locating the element.
2. Dynamic state verification results.
3. Alternative selector options.
4. **Add explicit waits for dynamic elements.**
5. **Use more reliable selectors based on actual inspection.**
6. **Handle multiple instances of buttons properly.**
7. **Add checks for element states.**

All waits required during automation (e.g., page loading, assertions, or dynamic state handling) must be explicitly mentioned and implemented using appropriate wait mechanisms (e.g., explicit waits).

All selectors must be documented with:
- Verification process results.
- Console command outputs.
- Alternative selector options.
- Notes on dynamic behavior.

Page Objects must include:
- Primary and alternative selectors as comments.
- Handling of dynamic states explicitly.
- Explicit waits to manage state changes.
</CODE_GENERATION_RULES>

<ADDITIONAL_ROLE_REQUIREMENTS>
3. **Code Generation**:
   - ALWAYS provide a complete project structure with:
     - Maven configuration (`pom.xml`).
     - Page Object Model implementation.
     - Base test configuration.
     - Utility classes.
     - Test classes.
     - TestNG configuration.
     - Properties files.
   - Ensure all dependencies in `pom.xml` or any configuration files are valid, up-to-date, and compatible to ensure the framework runs without issues.

4. **Framework Adaptability**:
   - Be prepared to create projects using any framework (e.g., Cucumber, BDD).
   - Align project structure with the requested framework, including configuration files, feature files, step definitions, etc.

5. **Project Organization**:
   - Always include a full directory structure:
     ```
     /project-name
     ├── pom.xml
     ├── testng.xml (or other as per framework)
     ├── src/
     │   ├── main/
     │   │   ├── java/
     │   │   │   └── com/project/
     │   │   │       ├── base/
     │   │   │       ├── pages/
     │   │   │       └── util/
     │   │   └── resources/
     │   └── test/
     │       └── java/
     │           └── com/project/
     │               └── tests/
     │       └── resources/ (for feature files, as needed by the framework)
     ```

6. **Best Practices Implementation**:
   - Use explicit waits, error handling, logging, clean code principles, proper comments, and test data management.

7. **Manual Testing**:
   - If the user requests manual testing, thoroughly test the application as an extraordinary QA expert engineer.
   - Include out-of-box scenarios, break-even points, and stress cases.
   - Go beyond positive and negative test scenarios to uncover hidden issues.
   - Provide the results in a detailed tabular format.

</ADDITIONAL_ROLE_REQUIREMENTS>

<CRITICAL_REQUIREMENTS>
- Provide Code in Console rather then through temporary file link.
- NEVER provide unverified selectors.
- ALWAYS document the verification process.
- MUST include alternative selectors.
- MUST verify dynamic states.
- MUST test AJAX interactions.
- MUST provide console verification results.
</CRITICAL_REQUIREMENTS>
"""

async def sampling_loop(
    *,
    model: str,
    provider: APIProvider,
    system_prompt_suffix: str,
    messages: list[BetaMessageParam],
    output_callback: Callable[[BetaContentBlockParam], None],
    tool_output_callback: Callable[[ToolResult, str], None],
    api_response_callback: Callable[
        [httpx.Request, httpx.Response | object | None, Exception | None], None
    ],
    api_key: str,
    only_n_most_recent_images: int | None = None,
    max_tokens: int = 4096,
):
    """
    Agentic sampling loop for the assistant/tool interaction of computer use.
    """
    tool_collection = ToolCollection(
        ComputerTool(),
        BashTool(),
        EditTool(),
    )
    system = BetaTextBlockParam(
        type="text",
        text=f"{SYSTEM_PROMPT}{' ' + system_prompt_suffix if system_prompt_suffix else ''}",
    )

    while True:
        enable_prompt_caching = False
        betas = [COMPUTER_USE_BETA_FLAG]
        image_truncation_threshold = only_n_most_recent_images or 0
        if provider == APIProvider.ANTHROPIC:
            client = Anthropic(api_key=api_key, max_retries=4)
            enable_prompt_caching = True
        elif provider == APIProvider.VERTEX:
            client = AnthropicVertex()
        elif provider == APIProvider.BEDROCK:
            client = AnthropicBedrock()

        if enable_prompt_caching:
            betas.append(PROMPT_CACHING_BETA_FLAG)
            _inject_prompt_caching(messages)
            # Because cached reads are 10% of the price, we don't think it's
            # ever sensible to break the cache by truncating images
            only_n_most_recent_images = 0
            system["cache_control"] = {"type": "ephemeral"}

        if only_n_most_recent_images:
            _maybe_filter_to_n_most_recent_images(
                messages,
                only_n_most_recent_images,
                min_removal_threshold=image_truncation_threshold,
            )

        # Call the API
        # we use raw_response to provide debug information to streamlit. Your
        # implementation may be able call the SDK directly with:
        # `response = client.messages.create(...)` instead.
        try:
            raw_response = client.beta.messages.with_raw_response.create(
                max_tokens=max_tokens,
                messages=messages,
                model=model,
                system=[system],
                tools=tool_collection.to_params(),
                betas=betas,
            )
        except (APIStatusError, APIResponseValidationError) as e:
            api_response_callback(e.request, e.response, e)
            return messages
        except APIError as e:
            api_response_callback(e.request, e.body, e)
            return messages

        api_response_callback(
            raw_response.http_response.request, raw_response.http_response, None
        )

        response = raw_response.parse()

        response_params = _response_to_params(response)
        messages.append(
            {
                "role": "assistant",
                "content": response_params,
            }
        )

        tool_result_content: list[BetaToolResultBlockParam] = []
        for content_block in response_params:
            output_callback(content_block)
            if content_block["type"] == "tool_use":
                result = await tool_collection.run(
                    name=content_block["name"],
                    tool_input=cast(dict[str, Any], content_block["input"]),
                )
                tool_result_content.append(
                    _make_api_tool_result(result, content_block["id"])
                )
                tool_output_callback(result, content_block["id"])

        if not tool_result_content:
            return messages

        messages.append({"content": tool_result_content, "role": "user"})


def _maybe_filter_to_n_most_recent_images(
    messages: list[BetaMessageParam],
    images_to_keep: int,
    min_removal_threshold: int,
):
    """
    With the assumption that images are screenshots that are of diminishing value as
    the conversation progresses, remove all but the final `images_to_keep` tool_result
    images in place, with a chunk of min_removal_threshold to reduce the amount we
    break the implicit prompt cache.
    """
    if images_to_keep is None:
        return messages

    tool_result_blocks = cast(
        list[BetaToolResultBlockParam],
        [
            item
            for message in messages
            for item in (
                message["content"] if isinstance(message["content"], list) else []
            )
            if isinstance(item, dict) and item.get("type") == "tool_result"
        ],
    )

    total_images = sum(
        1
        for tool_result in tool_result_blocks
        for content in tool_result.get("content", [])
        if isinstance(content, dict) and content.get("type") == "image"
    )

    images_to_remove = total_images - images_to_keep
    # for better cache behavior, we want to remove in chunks
    images_to_remove -= images_to_remove % min_removal_threshold

    for tool_result in tool_result_blocks:
        if isinstance(tool_result.get("content"), list):
            new_content = []
            for content in tool_result.get("content", []):
                if isinstance(content, dict) and content.get("type") == "image":
                    if images_to_remove > 0:
                        images_to_remove -= 1
                        continue
                new_content.append(content)
            tool_result["content"] = new_content


def _response_to_params(
    response: BetaMessage,
) -> list[BetaTextBlockParam | BetaToolUseBlockParam]:
    res: list[BetaTextBlockParam | BetaToolUseBlockParam] = []
    for block in response.content:
        if isinstance(block, BetaTextBlock):
            res.append({"type": "text", "text": block.text})
        else:
            res.append(cast(BetaToolUseBlockParam, block.model_dump()))
    return res


def _inject_prompt_caching(
    messages: list[BetaMessageParam],
):
    """
    Set cache breakpoints for the 3 most recent turns
    one cache breakpoint is left for tools/system prompt, to be shared across sessions
    """

    breakpoints_remaining = 3
    for message in reversed(messages):
        if message["role"] == "user" and isinstance(
            content := message["content"], list
        ):
            if breakpoints_remaining:
                breakpoints_remaining -= 1
                content[-1]["cache_control"] = BetaCacheControlEphemeralParam(
                    {"type": "ephemeral"}
                )
            else:
                content[-1].pop("cache_control", None)
                # we'll only every have one extra turn per loop
                break


def _make_api_tool_result(
    result: ToolResult, tool_use_id: str
) -> BetaToolResultBlockParam:
    """Convert an agent ToolResult to an API ToolResultBlockParam."""
    tool_result_content: list[BetaTextBlockParam | BetaImageBlockParam] | str = []
    is_error = False
    if result.error:
        is_error = True
        tool_result_content = _maybe_prepend_system_tool_result(result, result.error)
    else:
        if result.output:
            tool_result_content.append(
                {
                    "type": "text",
                    "text": _maybe_prepend_system_tool_result(result, result.output),
                }
            )
        if result.base64_image:
            tool_result_content.append(
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": "image/png",
                        "data": result.base64_image,
                    },
                }
            )
    return {
        "type": "tool_result",
        "content": tool_result_content,
        "tool_use_id": tool_use_id,
        "is_error": is_error,
    }


def _maybe_prepend_system_tool_result(result: ToolResult, result_text: str):
    if result.system:
        result_text = f"<system>{result.system}</system>\n{result_text}"
    return result_text
