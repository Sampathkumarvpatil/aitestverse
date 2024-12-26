## AI TestVerse

Natural Language Powered Testing Platform for writing tests in plain English. Describe what you want to test, and our AI understands and executes your requirements.

## Features

- **API TestVerse**: Test API performance and functionality using natural language
- **Web Performance Testing**: Analyze website performance with simple commands
- **ETL TestVerse**: Validate data transformations and quality checks  
- **JIRA Integration**: Manage JIRA tickets effortlessly
- **Automation Testing**: Automate testing workflows with natural language

## Prerequisites

- Node.js ≥ 14.0.0
- npm (comes with Node.js)
- Claude Desktop application

## Installation Methods

### 1. AI TestVerse Cloud
For enterprise installations with VPN access and enhanced security, contact us directly.

### 2. AI TestVerse MCP Installation

#### Claude Desktop Configuration Location
1. Open Claude Desktop
2. Click ☰ (top-left)
3. Navigate: File > Settings > Developer > Edit Config
4. Edit `claude_desktop_config.json`

**Important**: After configuration changes:
- Close Claude Desktop
- End process in Task Manager
- Restart application

#### Individual Agent Installation

##### API Performance Testing
```bash
npm install aitestverse-apiperformanceagent
```

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

##### Web Performance Testing
```bash
npm install aitestverse-webperformanceagent
```

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

##### ETL Testing
```bash
npm install aitestverse-etltestingagent
```

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

##### JIRA Integration
```bash
npm install aitestverse-jiraagent
```

```json
{
  "mcpServers": {
    "aitestverse-jira": {
      "command": "npx",
      "args": ["-y", "aitestverse-jiraagent"]
    }
  }
}
```

##### Automation Testing
```bash
npm install aitestverse-autoagent
```

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

#### Complete Configuration
Add to `claude_desktop_config.json`:

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
      "args": ["-y", "aitestverse-jiraagent"]
    },
    "aitestverse-auto": {
      "command": "npx",
      "args": ["-y", "aitestverse-autoagent"]
    }
  }
}
```

## Limitations

### API Testing Duration
- Claude Desktop: Maximum 3 minutes
- For longer tests:
  - Use AI TestVerse Cloud
  - Export K6 code and run locally

### Running K6 Tests Locally
```bash
# Install
npm install -g k6

# Basic run
k6 run test-script.js

# With duration
k6 run --duration 10m test-script.js

# With users
k6 run --vus 10 --duration 5m test-script.js
```

## Quick Start
1. Select testing domain
2. Install agent & configure
3. Write test in English
4. Execute and review results

## Documentation
- [API TestVerse](https://chatbotmaindocuments.s3.us-east-1.amazonaws.com/AI+API+TestVerse/index.html)
- [Web TestVerse](https://chatbotmaindocuments.s3.us-east-1.amazonaws.com/AI+Web+Testverse/index.html)
- [ETL TestVerse](https://chatbotmaindocuments.s3.us-east-1.amazonaws.com/AI+ETL+TestVerse/index.html)
- [JIRA TestVerse](https://chatbotmaindocuments.s3.us-east-1.amazonaws.com/AI+Jira+TestVerse/index.html)
- [AI TestVerse Platform](https://chatbotmaindocuments.s3.us-east-1.amazonaws.com/AI+TestVerse.html)

## License
© 2024 AI TestVerse. All rights reserved.
