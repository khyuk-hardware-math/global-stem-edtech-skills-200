---
name: repo-suneung-math-help
description: "tfoseel/math-help - 韩国资深教师针对修能数学杀手题编写的高级策略指南与函数图形"
category: github_ecosystem
repo: "tfoseel/math-help"
tech_stack: "TeX, Python"
domain: "Korea CSAT"
url: "https://github.com/tfoseel/math-help"
version: 1.0.0
---

# repo-suneung-math-help

> **GitHub 开源生态集成**: [tfoseel/math-help](https://github.com/tfoseel/math-help)
> 技术栈: `TeX, Python` | 业务领域: `Korea CSAT`

## 1. 仓库定位与核心资产
韩国资深教师针对修能数学杀手题编写的高级策略指南与函数图形

- **官方仓库地址**: [https://github.com/tfoseel/math-help](https://github.com/tfoseel/math-help)
- **技术选型与实现**: `TeX, Python`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/tfoseel/math-help.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-suneung-math-help --inspect-upstream
```
