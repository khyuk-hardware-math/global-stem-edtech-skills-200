---
name: repo-geogebra
description: "GeoGebra/geogebra - 全球数亿师生使用的动态几何与代数计算开源生态，支持 2D/3D 作图"
category: github_ecosystem
repo: "GeoGebra/geogebra"
tech_stack: "Java, JavaScript, WebAssembly"
domain: "Geometry"
url: "https://github.com/GeoGebra/geogebra"
version: 1.0.0
---

# repo-geogebra

> **GitHub 开源生态集成**: [GeoGebra/geogebra](https://github.com/GeoGebra/geogebra)
> 技术栈: `Java, JavaScript, WebAssembly` | 业务领域: `Geometry`

## 1. 仓库定位与核心资产
全球数亿师生使用的动态几何与代数计算开源生态，支持 2D/3D 作图

- **官方仓库地址**: [https://github.com/GeoGebra/geogebra](https://github.com/GeoGebra/geogebra)
- **技术选型与实现**: `Java, JavaScript, WebAssembly`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/GeoGebra/geogebra.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-geogebra --inspect-upstream
```
