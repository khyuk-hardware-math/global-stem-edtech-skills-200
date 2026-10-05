---
name: repo-kyodai-math-tex
description: "kyodai-math-tex/creative-solutions - 京都大学特色数学入试真题优雅解答与纯几何证明代码集"
category: github_ecosystem
repo: "kyodai-math-tex/creative-solutions"
tech_stack: "LaTeX, Asymptote"
domain: "Japan Kyodai"
url: "https://github.com/kyodai-math-tex/creative-solutions"
version: 1.0.0
---

# repo-kyodai-math-tex

> **GitHub 开源生态集成**: [kyodai-math-tex/creative-solutions](https://github.com/kyodai-math-tex/creative-solutions)
> 技术栈: `LaTeX, Asymptote` | 业务领域: `Japan Kyodai`

## 1. 仓库定位与核心资产
京都大学特色数学入试真题优雅解答与纯几何证明代码集

- **官方仓库地址**: [https://github.com/kyodai-math-tex/creative-solutions](https://github.com/kyodai-math-tex/creative-solutions)
- **技术选型与实现**: `LaTeX, Asymptote`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/kyodai-math-tex/creative-solutions.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-kyodai-math-tex --inspect-upstream
```
