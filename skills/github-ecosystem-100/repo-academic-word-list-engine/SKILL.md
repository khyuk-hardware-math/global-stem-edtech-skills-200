---
name: repo-academic-word-list-engine
description: "academic-word-list-awl-engine/core - Averil Coxhead 学术词汇表 (AWL) 570 词族构词法衍生与测试套件"
category: github_ecosystem
repo: "academic-word-list-awl-engine/core"
tech_stack: "Python, SQLite"
domain: "Academic Vocab"
url: "https://github.com/academic-word-list-awl-engine/core"
version: 1.0.0
---

# repo-academic-word-list-engine

> **GitHub 开源生态集成**: [academic-word-list-awl-engine/core](https://github.com/academic-word-list-awl-engine/core)
> 技术栈: `Python, SQLite` | 业务领域: `Academic Vocab`

## 1. 仓库定位与核心资产
Averil Coxhead 学术词汇表 (AWL) 570 词族构词法衍生与测试套件

- **官方仓库地址**: [https://github.com/academic-word-list-awl-engine/core](https://github.com/academic-word-list-awl-engine/core)
- **技术选型与实现**: `Python, SQLite`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/academic-word-list-awl-engine/core.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-academic-word-list-engine --inspect-upstream
```
