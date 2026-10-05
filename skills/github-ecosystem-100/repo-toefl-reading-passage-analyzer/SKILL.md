---
name: repo-toefl-reading-passage-analyzer
description: "toefl-reading-passage-analyzer/metrics - 统计托福学术文章句长分布、可读性指数与长难句抽离器"
category: github_ecosystem
repo: "toefl-reading-passage-analyzer/metrics"
tech_stack: "Python, NLTK"
domain: "TOEFL Reading"
url: "https://github.com/toefl-reading-passage-analyzer/metrics"
version: 1.0.0
---

# repo-toefl-reading-passage-analyzer

> **GitHub 开源生态集成**: [toefl-reading-passage-analyzer/metrics](https://github.com/toefl-reading-passage-analyzer/metrics)
> 技术栈: `Python, NLTK` | 业务领域: `TOEFL Reading`

## 1. 仓库定位与核心资产
统计托福学术文章句长分布、可读性指数与长难句抽离器

- **官方仓库地址**: [https://github.com/toefl-reading-passage-analyzer/metrics](https://github.com/toefl-reading-passage-analyzer/metrics)
- **技术选型与实现**: `Python, NLTK`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/toefl-reading-passage-analyzer/metrics.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-toefl-reading-passage-analyzer --inspect-upstream
```
