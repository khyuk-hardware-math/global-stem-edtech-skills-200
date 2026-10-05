---
name: repo-toefl-ibt-listening-practice
description: "toefl-ibt-listening-practice/app - 专为托福听力长讲座设计的康奈尔笔记双栏界面与分段精听跟读 Web"
category: github_ecosystem
repo: "toefl-ibt-listening-practice/app"
tech_stack: "React, Web Audio API"
domain: "TOEFL Listening"
url: "https://github.com/toefl-ibt-listening-practice/app"
version: 1.0.0
---

# repo-toefl-ibt-listening-practice

> **GitHub 开源生态集成**: [toefl-ibt-listening-practice/app](https://github.com/toefl-ibt-listening-practice/app)
> 技术栈: `React, Web Audio API` | 业务领域: `TOEFL Listening`

## 1. 仓库定位与核心资产
专为托福听力长讲座设计的康奈尔笔记双栏界面与分段精听跟读 Web

- **官方仓库地址**: [https://github.com/toefl-ibt-listening-practice/app](https://github.com/toefl-ibt-listening-practice/app)
- **技术选型与实现**: `React, Web Audio API`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/toefl-ibt-listening-practice/app.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-toefl-ibt-listening-practice --inspect-upstream
```
