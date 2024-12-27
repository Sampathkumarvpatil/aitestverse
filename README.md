# 🚀 AI TestVerse

&#x20;&#x20;

🤖 Write Tests in Plain English, Let AI Handle the Rest



---

## ✨ Features

| Feature | Description |
| ------- | ----------- |
| 🔄      |             |

| **API TestVerse**       | Test API performance with natural language |
| ----------------------- | ------------------------------------------ |
| 🌐 **Web Testing**      | Analyze website performance effortlessly   |
| 📊 **ETL TestVerse**    | Validate data transformations seamlessly   |
| 🎯 **JIRA Integration** | Manage tickets using plain English         |
| ⚡ **Automation**        | Automate workflows with simple commands    |

---

## 📚 Documentation

| **Service**           | **Description**                 | **Documentation** |
| --------------------- | ------------------------------- | ----------------- |
| 🚀 **Platform Guide** | Complete Platform Documentation |                   |
| 🔄 **API TestVerse**  | API Performance Testing         |                   |
| 🌐 **Web TestVerse**  | Web Performance Testing         |                   |
| 📊 **ETL TestVerse**  | Data Transformation Testing     |                   |
| 🎯 **JIRA TestVerse** | JIRA Automation                 |                   |

---

## 🛠️ Prerequisites



- Node.js ≥ 14.0.0
- npm (comes with Node.js)
- Claude Desktop application

---

## 💫 Installation Methods

### 🏢 1. AI TestVerse Cloud

> Enterprise-grade with VPN access and enhanced security. Contact us for setup.

### 🔧 2. AI TestVerse MCP Installation

#### 📝 Claude Desktop Configuration

1. Launch Claude Desktop
2. Click ☰ menu (top-left)
3. Navigate: `File > Settings > Developer > Edit Config`
4. Locate `claude_desktop_config.json`

> ⚠️ **Important**: After changes:
>
> - Close Claude Desktop
> - End process in Task Manager
> - Restart application

---

## 🚀 Quick Installation Guides

### 🔄 API Performance Testing

```bash
npm install aitestverse-apiperformanceagent
```

Configuration:

```json
{
  "mcpServers": {
    "aitestverse-api": {
      "command": "npx",
      "args": ["-y", "aitestverse-apiperformanceagent"]
    }
  }
}
```

### 🌐 Web Performance Testing

```bash
npm install aitestverse-webperformanceagent
```

Configuration:

```json
{
  "mcpServers": {
    "aitestverse-web": {
      "command": "npx",
      "args": ["-y", "aitestverse-webperformanceagent"]
    }
  }
}
```

### 📊 ETL Testing

```bash
npm install aitestverse-etltestingagent
```

Configuration:

```json
{
  "mcpServers": {
    "aitestverse-etl": {
      "command": "npx",
      "args": ["-y", "aitestverse-etltestingagent"]
    }
  }
}
```

### 🎯 JIRA Integration

```bash
npm install aitestverse-jiraagent
```

Configuration:

```json
{
  "mcpServers": {
    "aitestverse-jira": {
      "command": "npx",
      "args": [
        "-y",
        "--package=aitestverse-jiraagent",
        "aitestverse-jiraagent"
      ],
      "env": {
        "JIRA_URL": "<JIRA_BASE_URL>",
        "JIRA_USERNAME": "<YOUR_JIRA_USERNAME>",
        "JIRA_API_TOKEN": "<YOUR_JIRA_API_TOKEN>"
      }
    }
  }
}
```

**Parameters:**

- `<JIRA_BASE_URL>`: Your JIRA instance URL (e.g., `https://your-domain.atlassian.net`).
- `<YOUR_JIRA_USERNAME>`: The username of your JIRA account (e.g., `your-email@example.com`).
- `<YOUR_JIRA_API_TOKEN>`: Your JIRA API token. [Learn how to generate your API token](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/).

### ⚡ Automation Testing

```bash
npm install aitestverse-autoagent
```

Configuration:

```json
{
  "mcpServers": {
    "aitestverse-auto": {
      "command": "npx",
      "args": ["-y", "aitestverse-autoagent"]
    }
  }
}
```

---

## 🛠️ Overall Configuration

For comprehensive setup, you can define all required configurations in a single JSON object:

```json
{
  "mcpServers": {
    "aitestverse-api": {
      "command": "npx",
      "args": ["-y", "aitestverse-apiperformanceagent"]
    },
    "aitestverse-web": {
      "command": "npx",
      "args": ["-y", "aitestverse-webperformanceagent"]
    },
    "aitestverse-etl": {
      "command": "npx",
      "args": ["-y", "aitestverse-etltestingagent"]
    },
    "aitestverse-jira": {
      "command": "npx",
      "args": [
        "-y",
        "--package=aitestverse-jiraagent",
        "aitestverse-jiraagent"
      ],
      "env": {
        "JIRA_URL": "<JIRA_BASE_URL>",
        "JIRA_USERNAME": "<YOUR_JIRA_USERNAME>",
        "JIRA_API_TOKEN": "<YOUR_JIRA_API_TOKEN>"
      }
    },
    "aitestverse-auto": {
      "command": "npx",
      "args": ["-y", "aitestverse-autoagent"]
    }
  }
}
```

Replace placeholders like `<JIRA_BASE_URL>`, `<YOUR_JIRA_USERNAME>`, and `<YOUR_JIRA_API_TOKEN>` with your specific values for full system integration.

---

## ⚠️ Limitations

### API Testing Duration

- ⏱️ Claude Desktop: Maximum 3 minutes
- 🔄 For longer tests:
  - Use AI TestVerse Cloud
  - In Claude Desktop, for example, you can mention: Provide k6 code to simulate 1000 users for 5 minutes (use k6 code for any use case lasting more than 3 minutes) and run locally

### 🚀 Running K6 Tests Locally

Install K6:

```bash
npm install -g k6
```

Basic run:

```bash
k6 run test-script.js
```

---

### 🌟 Ready to revolutionize your testing? Get started now!

© 2024 AI TestVerse. All rights reserved.

