---
name: repo-jee-sciencestop
description: "yadevinit/JEE - 专门收录与深度剖析 JEE Advanced 历史上最难杀手题的攻坚项目"
category: github_ecosystem
repo: "yadevinit/JEE"
tech_stack: "Jupyter, Python, TeX"
domain: "India JEE"
url: "https://github.com/yadevinit/JEE"
version: 1.0.0
---

# repo-jee-sciencestop

> **GitHub 开源生态集成**: [yadevinit/JEE](https://github.com/yadevinit/JEE)
> 技术栈: `Jupyter, Python, TeX` | 业务领域: `India JEE`

## 1. 仓库定位与核心资产
专门收录与深度剖析 JEE Advanced 历史上最难杀手题的攻坚项目

- **官方仓库地址**: [https://github.com/yadevinit/JEE](https://github.com/yadevinit/JEE)
- **技术选型与实现**: `Jupyter, Python, TeX`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/yadevinit/JEE.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-jee-sciencestop --inspect-upstream
```
