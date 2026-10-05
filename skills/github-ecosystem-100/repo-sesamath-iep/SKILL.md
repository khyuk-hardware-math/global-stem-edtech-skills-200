---
name: repo-sesamath-iep
description: "sesamath/iep - 法国初中互动式几何尺规作图教研工具 (Instru-en-Poche)"
category: github_ecosystem
repo: "sesamath/iep"
tech_stack: "JavaScript, Canvas"
domain: "France Collège"
url: "https://github.com/sesamath/iep"
version: 1.0.0
---

# repo-sesamath-iep

> **GitHub 开源生态集成**: [sesamath/iep](https://github.com/sesamath/iep)
> 技术栈: `JavaScript, Canvas` | 业务领域: `France Collège`

## 1. 仓库定位与核心资产
法国初中互动式几何尺规作图教研工具 (Instru-en-Poche)

- **官方仓库地址**: [https://github.com/sesamath/iep](https://github.com/sesamath/iep)
- **技术选型与实现**: `JavaScript, Canvas`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/sesamath/iep.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-sesamath-iep --inspect-upstream
```
