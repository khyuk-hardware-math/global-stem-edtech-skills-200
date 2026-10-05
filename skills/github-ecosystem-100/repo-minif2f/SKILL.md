---
name: repo-minif2f
description: "openai/miniF2F - 面向形式化数学与自动定理证明的基准数据集，包含高中奥赛和高考真题"
category: github_ecosystem
repo: "openai/miniF2F"
tech_stack: "Lean 3/4, Isabelle"
domain: "Formal Math Benchmark"
url: "https://github.com/openai/miniF2F"
version: 1.0.0
---

# repo-minif2f

> **GitHub 开源生态集成**: [openai/miniF2F](https://github.com/openai/miniF2F)
> 技术栈: `Lean 3/4, Isabelle` | 业务领域: `Formal Math Benchmark`

## 1. 仓库定位与核心资产
面向形式化数学与自动定理证明的基准数据集，包含高中奥赛和高考真题

- **官方仓库地址**: [https://github.com/openai/miniF2F](https://github.com/openai/miniF2F)
- **技术选型与实现**: `Lean 3/4, Isabelle`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/openai/miniF2F.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-minif2f --inspect-upstream
```
