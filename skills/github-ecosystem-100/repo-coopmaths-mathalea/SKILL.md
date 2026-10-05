---
name: repo-coopmaths-mathalea
description: "coopmaths/mathalea - 法国教育部官方采纳的数学变参习题生成旗舰框架"
category: github_ecosystem
repo: "coopmaths/mathalea"
tech_stack: "TypeScript, Svelte, LaTeX"
domain: "France Bac"
url: "https://forge.apps.education.fr/coopmaths/mathalea"
version: 1.0.0
---

# repo-coopmaths-mathalea

> **GitHub 开源生态集成**: [coopmaths/mathalea](https://forge.apps.education.fr/coopmaths/mathalea)
> 技术栈: `TypeScript, Svelte, LaTeX` | 业务领域: `France Bac`

## 1. 仓库定位与核心资产
法国教育部官方采纳的数学变参习题生成旗舰框架

- **官方仓库地址**: [https://forge.apps.education.fr/coopmaths/mathalea](https://forge.apps.education.fr/coopmaths/mathalea)
- **技术选型与实现**: `TypeScript, Svelte, LaTeX`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://forge.apps.education.fr/coopmaths/mathalea.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-coopmaths-mathalea --inspect-upstream
```
