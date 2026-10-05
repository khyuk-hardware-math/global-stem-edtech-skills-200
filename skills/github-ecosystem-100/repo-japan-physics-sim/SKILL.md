---
name: repo-japan-physics-sim
description: "japan-physics-sim/koukou-butsuri - 面向日本高校物理教材力学、波动、电磁学的交互式 HTML5 实验展示"
category: github_ecosystem
repo: "japan-physics-sim/koukou-butsuri"
tech_stack: "JavaScript, p5.js"
domain: "Japan Physics"
url: "https://github.com/japan-physics-sim/koukou-butsuri"
version: 1.0.0
---

# repo-japan-physics-sim

> **GitHub 开源生态集成**: [japan-physics-sim/koukou-butsuri](https://github.com/japan-physics-sim/koukou-butsuri)
> 技术栈: `JavaScript, p5.js` | 业务领域: `Japan Physics`

## 1. 仓库定位与核心资产
面向日本高校物理教材力学、波动、电磁学的交互式 HTML5 实验展示

- **官方仓库地址**: [https://github.com/japan-physics-sim/koukou-butsuri](https://github.com/japan-physics-sim/koukou-butsuri)
- **技术选型与实现**: `JavaScript, p5.js`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/japan-physics-sim/koukou-butsuri.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-japan-physics-sim --inspect-upstream
```
