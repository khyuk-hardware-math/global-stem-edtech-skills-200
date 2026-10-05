---
name: repo-typst
description: "typst/typst - 现代化可编程排版引擎，编译速度比 LaTeX 快百倍的考卷排版神器"
category: github_ecosystem
repo: "typst/typst"
tech_stack: "Rust, C++"
domain: "Modern Typesetting"
url: "https://github.com/typst/typst"
version: 1.0.0
---

# repo-typst

> **GitHub 开源生态集成**: [typst/typst](https://github.com/typst/typst)
> 技术栈: `Rust, C++` | 业务领域: `Modern Typesetting`

## 1. 仓库定位与核心资产
现代化可编程排版引擎，编译速度比 LaTeX 快百倍的考卷排版神器

- **官方仓库地址**: [https://github.com/typst/typst](https://github.com/typst/typst)
- **技术选型与实现**: `Rust, C++`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/typst/typst.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-typst --inspect-upstream
```
