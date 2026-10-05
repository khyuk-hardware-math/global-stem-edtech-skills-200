---
name: repo-coopmaths-apigeom
description: "coopmaths/apiGeom - CoopMaths 配套几何作图与交互引擎，支持网页动态拖拽点与线段"
category: github_ecosystem
repo: "coopmaths/apiGeom"
tech_stack: "TypeScript, Canvas"
domain: "France Math"
url: "https://github.com/coopmaths/apiGeom"
version: 1.0.0
---

# repo-coopmaths-apigeom

> **GitHub 开源生态集成**: [coopmaths/apiGeom](https://github.com/coopmaths/apiGeom)
> 技术栈: `TypeScript, Canvas` | 业务领域: `France Math`

## 1. 仓库定位与核心资产
CoopMaths 配套几何作图与交互引擎，支持网页动态拖拽点与线段

- **官方仓库地址**: [https://github.com/coopmaths/apiGeom](https://github.com/coopmaths/apiGeom)
- **技术选型与实现**: `TypeScript, Canvas`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/coopmaths/apiGeom.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-coopmaths-apigeom --inspect-upstream
```
