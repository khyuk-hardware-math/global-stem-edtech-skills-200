---
name: repo-threejs
description: "mrdoob/three.js - 最流行的 Web 3D 渲染库，用于浏览器中立体几何与物理空间演示"
category: github_ecosystem
repo: "mrdoob/three.js"
tech_stack: "JavaScript, WebGL, WebGPU"
domain: "3D Visualization"
url: "https://github.com/mrdoob/three.js"
version: 1.0.0
---

# repo-threejs

> **GitHub 开源生态集成**: [mrdoob/three.js](https://github.com/mrdoob/three.js)
> 技术栈: `JavaScript, WebGL, WebGPU` | 业务领域: `3D Visualization`

## 1. 仓库定位与核心资产
最流行的 Web 3D 渲染库，用于浏览器中立体几何与物理空间演示

- **官方仓库地址**: [https://github.com/mrdoob/three.js](https://github.com/mrdoob/three.js)
- **技术选型与实现**: `JavaScript, WebGL, WebGPU`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/mrdoob/three.js.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-threejs --inspect-upstream
```
