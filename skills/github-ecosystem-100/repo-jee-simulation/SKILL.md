---
name: repo-jee-simulation
description: "akshdeepsingh7/Jee-Simulation - 全真还原印度 NTA 真实机考环境的模拟考场与计时器"
category: github_ecosystem
repo: "akshdeepsingh7/Jee-Simulation"
tech_stack: "JavaScript, HTML5"
domain: "India JEE"
url: "https://github.com/akshdeepsingh7/Jee-Simulation"
version: 1.0.0
---

# repo-jee-simulation

> **GitHub 开源生态集成**: [akshdeepsingh7/Jee-Simulation](https://github.com/akshdeepsingh7/Jee-Simulation)
> 技术栈: `JavaScript, HTML5` | 业务领域: `India JEE`

## 1. 仓库定位与核心资产
全真还原印度 NTA 真实机考环境的模拟考场与计时器

- **官方仓库地址**: [https://github.com/akshdeepsingh7/Jee-Simulation](https://github.com/akshdeepsingh7/Jee-Simulation)
- **技术选型与实现**: `JavaScript, HTML5`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/akshdeepsingh7/Jee-Simulation.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-jee-simulation --inspect-upstream
```
