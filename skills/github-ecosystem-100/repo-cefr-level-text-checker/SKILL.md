---
name: repo-cefr-level-text-checker
description: "cefr-level-text-checker/core - 依据欧洲共同语言参考标准 (CEFR) 自动分析任意英文难度的分析仪"
category: github_ecosystem
repo: "cefr-level-text-checker/core"
tech_stack: "Python, spaCy, NLTK"
domain: "CEFR Assessment"
url: "https://github.com/cefr-level-text-checker/core"
version: 1.0.0
---

# repo-cefr-level-text-checker

> **GitHub 开源生态集成**: [cefr-level-text-checker/core](https://github.com/cefr-level-text-checker/core)
> 技术栈: `Python, spaCy, NLTK` | 业务领域: `CEFR Assessment`

## 1. 仓库定位与核心资产
依据欧洲共同语言参考标准 (CEFR) 自动分析任意英文难度的分析仪

- **官方仓库地址**: [https://github.com/cefr-level-text-checker/core](https://github.com/cefr-level-text-checker/core)
- **技术选型与实现**: `Python, spaCy, NLTK`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/cefr-level-text-checker/core.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-cefr-level-text-checker --inspect-upstream
```
