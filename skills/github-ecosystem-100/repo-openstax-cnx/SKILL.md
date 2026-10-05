---
name: repo-openstax-cnx
description: "OpenStax/cnx - 莱斯大学 OpenStax 开源大学与 AP 预备数理化教科书平台"
category: github_ecosystem
repo: "OpenStax/cnx"
tech_stack: "Python, JavaScript"
domain: "AP / University"
url: "https://github.com/OpenStax/cnx"
version: 1.0.0
---

# repo-openstax-cnx

> **GitHub 开源生态集成**: [OpenStax/cnx](https://github.com/OpenStax/cnx)
> 技术栈: `Python, JavaScript` | 业务领域: `AP / University`

## 1. 仓库定位与核心资产
莱斯大学 OpenStax 开源大学与 AP 预备数理化教科书平台

- **官方仓库地址**: [https://github.com/OpenStax/cnx](https://github.com/OpenStax/cnx)
- **技术选型与实现**: `Python, JavaScript`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/OpenStax/cnx.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-openstax-cnx --inspect-upstream
```
