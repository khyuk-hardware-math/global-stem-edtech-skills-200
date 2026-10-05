---
name: repo-torobo-solver
description: "nii-todai-robot/torobo-solver - 日本国立情报学研究所 (NII) 东大机器人项目的数理求解组件"
category: github_ecosystem
repo: "nii-todai-robot/torobo-solver"
tech_stack: "Lisp, Python, Maxima"
domain: "Japan Todai"
url: "https://github.com/nii-todai-robot/torobo-solver"
version: 1.0.0
---

# repo-torobo-solver

> **GitHub 开源生态集成**: [nii-todai-robot/torobo-solver](https://github.com/nii-todai-robot/torobo-solver)
> 技术栈: `Lisp, Python, Maxima` | 业务领域: `Japan Todai`

## 1. 仓库定位与核心资产
日本国立情报学研究所 (NII) 东大机器人项目的数理求解组件

- **官方仓库地址**: [https://github.com/nii-todai-robot/torobo-solver](https://github.com/nii-todai-robot/torobo-solver)
- **技术选型与实现**: `Lisp, Python, Maxima`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/nii-todai-robot/torobo-solver.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-torobo-solver --inspect-upstream
```
