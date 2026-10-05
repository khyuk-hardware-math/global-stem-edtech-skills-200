---
name: repo-esl-interactive-flashcards
description: "esl-interactive-flashcards/web-app - 面向青少儿英语教学的高交互 Web 闪卡游戏（翻转/配对/听辨）"
category: github_ecosystem
repo: "esl-interactive-flashcards/web-app"
tech_stack: "Vue.js, TailwindCSS"
domain: "ESL Flashcards"
url: "https://github.com/esl-interactive-flashcards/web-app"
version: 1.0.0
---

# repo-esl-interactive-flashcards

> **GitHub 开源生态集成**: [esl-interactive-flashcards/web-app](https://github.com/esl-interactive-flashcards/web-app)
> 技术栈: `Vue.js, TailwindCSS` | 业务领域: `ESL Flashcards`

## 1. 仓库定位与核心资产
面向青少儿英语教学的高交互 Web 闪卡游戏（翻转/配对/听辨）

- **官方仓库地址**: [https://github.com/esl-interactive-flashcards/web-app](https://github.com/esl-interactive-flashcards/web-app)
- **技术选型与实现**: `Vue.js, TailwindCSS`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/esl-interactive-flashcards/web-app.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-esl-interactive-flashcards --inspect-upstream
```
