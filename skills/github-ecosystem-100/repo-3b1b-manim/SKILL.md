---
name: repo-3b1b-manim
description: "3b1b/manim - Grant Sanderson (3Blue1Brown) 核心个人底层数学动画代码库"
category: github_ecosystem
repo: "3b1b/manim"
tech_stack: "Python, ModernGL"
domain: "Math Aesthetic"
url: "https://github.com/3b1b/manim"
version: 1.0.0
---

# repo-3b1b-manim

> **GitHub 开源生态集成**: [3b1b/manim](https://github.com/3b1b/manim)
> 技术栈: `Python, ModernGL` | 业务领域: `Math Aesthetic`

## 1. 仓库定位与核心资产
Grant Sanderson (3Blue1Brown) 核心个人底层数学动画代码库

- **官方仓库地址**: [https://github.com/3b1b/manim](https://github.com/3b1b/manim)
- **技术选型与实现**: `Python, ModernGL`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/3b1b/manim.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-3b1b-manim --inspect-upstream
```
