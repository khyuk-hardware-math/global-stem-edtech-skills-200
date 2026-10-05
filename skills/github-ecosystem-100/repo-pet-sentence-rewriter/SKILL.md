---
name: repo-pet-sentence-rewriter
description: "pet-sentence-rewriter/paraphrase-ai - PET 核心考点同义句转换自动训练与即时反馈纠错工具"
category: github_ecosystem
repo: "pet-sentence-rewriter/paraphrase-ai"
tech_stack: "Python, Transformers"
domain: "Cambridge PET"
url: "https://github.com/pet-sentence-rewriter/paraphrase-ai"
version: 1.0.0
---

# repo-pet-sentence-rewriter

> **GitHub 开源生态集成**: [pet-sentence-rewriter/paraphrase-ai](https://github.com/pet-sentence-rewriter/paraphrase-ai)
> 技术栈: `Python, Transformers` | 业务领域: `Cambridge PET`

## 1. 仓库定位与核心资产
PET 核心考点同义句转换自动训练与即时反馈纠错工具

- **官方仓库地址**: [https://github.com/pet-sentence-rewriter/paraphrase-ai](https://github.com/pet-sentence-rewriter/paraphrase-ai)
- **技术选型与实现**: `Python, Transformers`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/pet-sentence-rewriter/paraphrase-ai.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-pet-sentence-rewriter --inspect-upstream
```
