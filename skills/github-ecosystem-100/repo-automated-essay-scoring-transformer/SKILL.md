---
name: repo-automated-essay-scoring-transformer
description: "F-Fer/automated_essay_scoring - 采用 Transformer 架构的雅思 Task 2 作文自动化多维指标评测系统"
category: github_ecosystem
repo: "F-Fer/automated_essay_scoring"
tech_stack: "Python, HuggingFace, BERT"
domain: "IELTS Writing"
url: "https://github.com/F-Fer/automated_essay_scoring"
version: 1.0.0
---

# repo-automated-essay-scoring-transformer

> **GitHub 开源生态集成**: [F-Fer/automated_essay_scoring](https://github.com/F-Fer/automated_essay_scoring)
> 技术栈: `Python, HuggingFace, BERT` | 业务领域: `IELTS Writing`

## 1. 仓库定位与核心资产
采用 Transformer 架构的雅思 Task 2 作文自动化多维指标评测系统

- **官方仓库地址**: [https://github.com/F-Fer/automated_essay_scoring](https://github.com/F-Fer/automated_essay_scoring)
- **技术选型与实现**: `Python, HuggingFace, BERT`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/F-Fer/automated_essay_scoring.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-automated-essay-scoring-transformer --inspect-upstream
```
