---
name: repo-phetsims-core
description: "phetsims/phet-core - 科罗拉多大学著名的 PhET 互动仿真模拟项目底层框架"
category: github_ecosystem
repo: "phetsims/phet-core"
tech_stack: "JavaScript, HTML5 Canvas"
domain: "Virtual Labs"
url: "https://github.com/phetsims/phet-core"
version: 1.0.0
---

# repo-phetsims-core

> **GitHub 开源生态集成**: [phetsims/phet-core](https://github.com/phetsims/phet-core)
> 技术栈: `JavaScript, HTML5 Canvas` | 业务领域: `Virtual Labs`

## 1. 仓库定位与核心资产
科罗拉多大学著名的 PhET 互动仿真模拟项目底层框架

- **官方仓库地址**: [https://github.com/phetsims/phet-core](https://github.com/phetsims/phet-core)
- **技术选型与实现**: `JavaScript, HTML5 Canvas`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/phetsims/phet-core.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-phetsims-core --inspect-upstream
```
