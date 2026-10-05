---
name: repo-todai-math-archive
description: "todai-math-tex/archive-1960-2025 - 收录东京大学半个世纪以来理科与文科数学入试真题的 TeX 整理项目"
category: github_ecosystem
repo: "todai-math-tex/archive-1960-2025"
tech_stack: "LaTeX, BibTeX"
domain: "Japan Todai"
url: "https://github.com/todai-math-tex/archive-1960-2025"
version: 1.0.0
---

# repo-todai-math-archive

> **GitHub 开源生态集成**: [todai-math-tex/archive-1960-2025](https://github.com/todai-math-tex/archive-1960-2025)
> 技术栈: `LaTeX, BibTeX` | 业务领域: `Japan Todai`

## 1. 仓库定位与核心资产
收录东京大学半个世纪以来理科与文科数学入试真题的 TeX 整理项目

- **官方仓库地址**: [https://github.com/todai-math-tex/archive-1960-2025](https://github.com/todai-math-tex/archive-1960-2025)
- **技术选型与实现**: `LaTeX, BibTeX`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/todai-math-tex/archive-1960-2025.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-todai-math-archive --inspect-upstream
```
