---
name: repo-katex
description: "Khan/KaTeX - 可汗学院出品的极速 Web 数学公式排版引擎，每秒渲染数千个公式"
category: github_ecosystem
repo: "Khan/KaTeX"
tech_stack: "JavaScript"
domain: "Math Typesetting"
url: "https://github.com/Khan/KaTeX"
version: 1.0.0
---

# repo-katex

> **GitHub 开源生态集成**: [Khan/KaTeX](https://github.com/Khan/KaTeX)
> 技术栈: `JavaScript` | 业务领域: `Math Typesetting`

## 1. 仓库定位与核心资产
可汗学院出品的极速 Web 数学公式排版引擎，每秒渲染数千个公式

- **官方仓库地址**: [https://github.com/Khan/KaTeX](https://github.com/Khan/KaTeX)
- **技术选型与实现**: `JavaScript`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/Khan/KaTeX.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-katex --inspect-upstream
```
