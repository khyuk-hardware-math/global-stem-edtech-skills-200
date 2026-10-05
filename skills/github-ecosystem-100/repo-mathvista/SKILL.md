---
name: repo-mathvista
description: "microsoft/MathVista - 微软推出的包含几何图、函数图与示意图的开创性视觉数学大模型基准"
category: github_ecosystem
repo: "microsoft/MathVista"
tech_stack: "Python, PyTorch"
domain: "Multimodal Math"
url: "https://github.com/microsoft/MathVista"
version: 1.0.0
---

# repo-mathvista

> **GitHub 开源生态集成**: [microsoft/MathVista](https://github.com/microsoft/MathVista)
> 技术栈: `Python, PyTorch` | 业务领域: `Multimodal Math`

## 1. 仓库定位与核心资产
微软推出的包含几何图、函数图与示意图的开创性视觉数学大模型基准

- **官方仓库地址**: [https://github.com/microsoft/MathVista](https://github.com/microsoft/MathVista)
- **技术选型与实现**: `Python, PyTorch`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/microsoft/MathVista.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-mathvista --inspect-upstream
```
