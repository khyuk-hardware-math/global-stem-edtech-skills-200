---
name: repo-prairielearn
description: "PrairieLearn/PrairieLearn - UIUC 开源的掌握性在线数理作业与机考自动评分平台"
category: github_ecosystem
repo: "PrairieLearn/PrairieLearn"
tech_stack: "Node.js, Python, PostgreSQL"
domain: "University / STEM"
url: "https://github.com/PrairieLearn/PrairieLearn"
version: 1.0.0
---

# repo-prairielearn

> **GitHub 开源生态集成**: [PrairieLearn/PrairieLearn](https://github.com/PrairieLearn/PrairieLearn)
> 技术栈: `Node.js, Python, PostgreSQL` | 业务领域: `University / STEM`

## 1. 仓库定位与核心资产
UIUC 开源的掌握性在线数理作业与机考自动评分平台

- **官方仓库地址**: [https://github.com/PrairieLearn/PrairieLearn](https://github.com/PrairieLearn/PrairieLearn)
- **技术选型与实现**: `Node.js, Python, PostgreSQL`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/PrairieLearn/PrairieLearn.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-prairielearn --inspect-upstream
```
