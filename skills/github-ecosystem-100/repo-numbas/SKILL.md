---
name: repo-numbas
description: "numbas/Numbas - 英国纽卡斯尔大学开发的开源富媒体数学在线测评系统"
category: github_ecosystem
repo: "numbas/Numbas"
tech_stack: "JavaScript, Python"
domain: "UK GCSE/A-Level"
url: "https://github.com/numbas/Numbas"
version: 1.0.0
---

# repo-numbas

> **GitHub 开源生态集成**: [numbas/Numbas](https://github.com/numbas/Numbas)
> 技术栈: `JavaScript, Python` | 业务领域: `UK GCSE/A-Level`

## 1. 仓库定位与核心资产
英国纽卡斯尔大学开发的开源富媒体数学在线测评系统

- **官方仓库地址**: [https://github.com/numbas/Numbas](https://github.com/numbas/Numbas)
- **技术选型与实现**: `JavaScript, Python`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/numbas/Numbas.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-numbas --inspect-upstream
```
