---
name: repo-capytale
description: "education-nationale/capytale - 法国教育部全国部署的初高中编程与数理在线 Notebook"
category: github_ecosystem
repo: "education-nationale/capytale"
tech_stack: "Python, Jupyter, Vue.js"
domain: "France Official"
url: "https://github.com/education-nationale/capytale"
version: 1.0.0
---

# repo-capytale

> **GitHub 开源生态集成**: [education-nationale/capytale](https://github.com/education-nationale/capytale)
> 技术栈: `Python, Jupyter, Vue.js` | 业务领域: `France Official`

## 1. 仓库定位与核心资产
法国教育部全国部署的初高中编程与数理在线 Notebook

- **官方仓库地址**: [https://github.com/education-nationale/capytale](https://github.com/education-nationale/capytale)
- **技术选型与实现**: `Python, Jupyter, Vue.js`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/education-nationale/capytale.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-capytale --inspect-upstream
```
