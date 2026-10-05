---
name: repo-jeechallenger
description: "Samya-S/jeechallenger-app - JEE 备考全功能 Web 应用，集成历年真题模拟与 AI 辅导"
category: github_ecosystem
repo: "Samya-S/jeechallenger-app"
tech_stack: "React, Node.js"
domain: "India JEE"
url: "https://github.com/Samya-S/jeechallenger-app"
version: 1.0.0
---

# repo-jeechallenger

> **GitHub 开源生态集成**: [Samya-S/jeechallenger-app](https://github.com/Samya-S/jeechallenger-app)
> 技术栈: `React, Node.js` | 业务领域: `India JEE`

## 1. 仓库定位与核心资产
JEE 备考全功能 Web 应用，集成历年真题模拟与 AI 辅导

- **官方仓库地址**: [https://github.com/Samya-S/jeechallenger-app](https://github.com/Samya-S/jeechallenger-app)
- **技术选型与实现**: `React, Node.js`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/Samya-S/jeechallenger-app.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-jeechallenger --inspect-upstream
```
