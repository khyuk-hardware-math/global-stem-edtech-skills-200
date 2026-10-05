---
name: repo-mathlib4
description: "leanprover-community/mathlib4 - 形式化数学与交互式定理证明器 Lean 4 的官方数学库"
category: github_ecosystem
repo: "leanprover-community/mathlib4"
tech_stack: "Lean 4, C++"
domain: "Formal Proof"
url: "https://github.com/leanprover-community/mathlib4"
version: 1.0.0
---

# repo-mathlib4

> **GitHub 开源生态集成**: [leanprover-community/mathlib4](https://github.com/leanprover-community/mathlib4)
> 技术栈: `Lean 4, C++` | 业务领域: `Formal Proof`

## 1. 仓库定位与核心资产
形式化数学与交互式定理证明器 Lean 4 的官方数学库

- **官方仓库地址**: [https://github.com/leanprover-community/mathlib4](https://github.com/leanprover-community/mathlib4)
- **技术选型与实现**: `Lean 4, C++`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/leanprover-community/mathlib4.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-mathlib4 --inspect-upstream
```
