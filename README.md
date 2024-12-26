<div align="center">

# 🚀 AI TestVerse

<img src="https://img.shields.io/badge/version-1.0.0-blue.svg" alt="version"/>
<img src="https://img.shields.io/badge/npm-%3E%3D%206.0.0-blue.svg" alt="npm"/>
<img src="https://img.shields.io/badge/node-%3E%3D%2014.0.0-blue.svg" alt="node"/>

> 🤖 Write Tests in Plain English, Let AI Handle the Rest

</div>

---

## ✨ Features

| Feature | Description |
|---------|------------|
| 🔄 **API TestVerse** | Test API performance with natural language |
| 🌐 **Web Testing** | Analyze website performance effortlessly |
| 📊 **ETL TestVerse** | Validate data transformations seamlessly |
| 🎯 **JIRA Integration** | Manage tickets using plain English |
| ⚡ **Automation** | Automate workflows with simple commands |

---

## 📚 Documentation

| **Service**            | **Description**               | **Documentation**                                                                                                     |
|-------------------------|-------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| 🔄 **API TestVerse**    | API Performance Testing       | [![View Docs](https://img.shields.io/badge/View-Docs-blue)](https://chatbotmaindocuments.s3.us-east-1.amazonaws.com/AI+API+TestVerse/index.html)  |
| 🌐 **Web TestVerse**    | Web Performance Testing       | [![View Docs](https://img.shields.io/badge/View-Docs-blue)](https://chatbotmaindocuments.s3.us-east-1.amazonaws.com/AI+Web+Testverse/index.html) |
| 📊 **ETL TestVerse**    | Data Transformation Testing   | [![View Docs](https://img.shields.io/badge/View-Docs-blue)](https://chatbotmaindocuments.s3.us-east-1.amazonaws.com/AI+ETL+TestVerse/index.html) |
| 🎯 **JIRA TestVerse**   | JIRA Automation               | [![View Docs](https://img.shields.io/badge/View-Docs-blue)](https://chatbotmaindocuments.s3.us-east-1.amazonaws.com/AI+Jira+TestVerse/index.html) |
| 🚀 **Platform Guide**   | Complete Platform Documentation | [![View Docs](https://img.shields.io/badge/View-Docs-blue)](https://chatbotmaindocuments.s3.us-east-1.amazonaws.com/AI+TestVerse.html)           |

---

## 🛠️ Prerequisites

![Tech Stack](https://img.shields.io/badge/Tech%20Stack-Modern-blue)

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

> ⚠️ **Important**: After changes
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
      "args": ["-y", "aitestverse-jiraagent"]
    }
  }
}
```

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

With duration:
```bash
k6 run --duration 10m test-script.js
```

With users:
```bash
k6 run --vus 10 --duration 5m test-script.js
```

---

<div align="center">

### 🌟 Ready to revolutionize your testing? Get started now! 

© 2024 AI TestVerse. All rights reserved.
</div>
