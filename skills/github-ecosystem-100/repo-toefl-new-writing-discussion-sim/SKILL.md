---
name: repo-toefl-new-writing-discussion-sim
description: "toefl-new-writing-discussion-sim/client - 针对托福改革后学术讨论写作 (Academic Discussion) 的模拟答题器"
category: github_ecosystem
repo: "toefl-new-writing-discussion-sim/client"
tech_stack: "Vue.js, TailwindCSS"
domain: "TOEFL Writing"
url: "https://github.com/toefl-new-writing-discussion-sim/client"
version: 1.0.0
---

# repo-toefl-new-writing-discussion-sim

> **GitHub 开源生态集成**: [toefl-new-writing-discussion-sim/client](https://github.com/toefl-new-writing-discussion-sim/client)
> 技术栈: `Vue.js, TailwindCSS` | 业务领域: `TOEFL Writing`

## 1. 仓库定位与核心资产
针对托福改革后学术讨论写作 (Academic Discussion) 的模拟答题器

- **官方仓库地址**: [https://github.com/toefl-new-writing-discussion-sim/client](https://github.com/toefl-new-writing-discussion-sim/client)
- **技术选型与实现**: `Vue.js, TailwindCSS`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/toefl-new-writing-discussion-sim/client.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-toefl-new-writing-discussion-sim --inspect-upstream
```
