---
name: repo-oxford-3000-5000-vocab
description: "oxford-3000-5000-vocabulary-dataset/db - 牛津核心 3000/5000 词与 CEFR 难度标签的高质量开源数据集"
category: github_ecosystem
repo: "oxford-3000-5000-vocabulary-dataset/db"
tech_stack: "CSV, SQLite"
domain: "Vocabulary DB"
url: "https://github.com/oxford-3000-5000-vocabulary-dataset/db"
version: 1.0.0
---

# repo-oxford-3000-5000-vocab

> **GitHub 开源生态集成**: [oxford-3000-5000-vocabulary-dataset/db](https://github.com/oxford-3000-5000-vocabulary-dataset/db)
> 技术栈: `CSV, SQLite` | 业务领域: `Vocabulary DB`

## 1. 仓库定位与核心资产
牛津核心 3000/5000 词与 CEFR 难度标签的高质量开源数据集

- **官方仓库地址**: [https://github.com/oxford-3000-5000-vocabulary-dataset/db](https://github.com/oxford-3000-5000-vocabulary-dataset/db)
- **技术选型与实现**: `CSV, SQLite`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/oxford-3000-5000-vocabulary-dataset/db.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-oxford-3000-5000-vocab --inspect-upstream
```
