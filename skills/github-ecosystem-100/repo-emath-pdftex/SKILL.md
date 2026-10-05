---
name: repo-emath-pdftex
description: "takotakot/emath-pdftex - 日本高校数学教师广泛使用的 emath LaTeX 考卷宏包"
category: github_ecosystem
repo: "takotakot/emath-pdftex"
tech_stack: "TeX, Perl, PostScript"
domain: "Japan Math"
url: "https://github.com/takotakot/emath-pdftex"
version: 1.0.0
---

# repo-emath-pdftex

> **GitHub 开源生态集成**: [takotakot/emath-pdftex](https://github.com/takotakot/emath-pdftex)
> 技术栈: `TeX, Perl, PostScript` | 业务领域: `Japan Math`

## 1. 仓库定位与核心资产
日本高校数学教师广泛使用的 emath LaTeX 考卷宏包

- **官方仓库地址**: [https://github.com/takotakot/emath-pdftex](https://github.com/takotakot/emath-pdftex)
- **技术选型与实现**: `TeX, Perl, PostScript`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/takotakot/emath-pdftex.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-emath-pdftex --inspect-upstream
```
