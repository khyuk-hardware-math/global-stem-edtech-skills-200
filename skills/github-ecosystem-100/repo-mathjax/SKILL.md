---
name: repo-mathjax
description: "mathjax/MathJax - 跨浏览器的工业级全功能数学排版显示引擎，支持 MathML、LaTeX"
category: github_ecosystem
repo: "mathjax/MathJax"
tech_stack: "JavaScript"
domain: "Math Typesetting"
url: "https://github.com/mathjax/MathJax"
version: 1.0.0
---

# repo-mathjax

> **GitHub 开源生态集成**: [mathjax/MathJax](https://github.com/mathjax/MathJax)
> 技术栈: `JavaScript` | 业务领域: `Math Typesetting`

## 1. 仓库定位与核心资产
跨浏览器的工业级全功能数学排版显示引擎，支持 MathML、LaTeX

- **官方仓库地址**: [https://github.com/mathjax/MathJax](https://github.com/mathjax/MathJax)
- **技术选型与实现**: `JavaScript`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/mathjax/MathJax.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-mathjax --inspect-upstream
```
