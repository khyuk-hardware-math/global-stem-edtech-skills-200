---
name: repo-suneung-killer-solver
description: "suneung-killer-solver/calculus-differential - 专门推演修能数学 22 题和 30 题多项式切线与极点分类模型"
category: github_ecosystem
repo: "suneung-killer-solver/calculus-differential"
tech_stack: "Python, SymPy"
domain: "Korea Math"
url: "https://github.com/suneung-killer-solver/calculus-differential"
version: 1.0.0
---

# repo-suneung-killer-solver

> **GitHub 开源生态集成**: [suneung-killer-solver/calculus-differential](https://github.com/suneung-killer-solver/calculus-differential)
> 技术栈: `Python, SymPy` | 业务领域: `Korea Math`

## 1. 仓库定位与核心资产
专门推演修能数学 22 题和 30 题多项式切线与极点分类模型

- **官方仓库地址**: [https://github.com/suneung-killer-solver/calculus-differential](https://github.com/suneung-killer-solver/calculus-differential)
- **技术选型与实现**: `Python, SymPy`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/suneung-killer-solver/calculus-differential.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-suneung-killer-solver --inspect-upstream
```
