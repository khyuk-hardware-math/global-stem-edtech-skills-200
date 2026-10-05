---
name: repo-grand-oral-stem
description: "epreuves-orales-bac/grand-oral-stem - 针对法国高考大口试 (Grand Oral) 数理方向的选题库与答辩模板"
category: github_ecosystem
repo: "epreuves-orales-bac/grand-oral-stem"
tech_stack: "Markdown, PDF"
domain: "France Bac"
url: "https://github.com/epreuves-orales-bac/grand-oral-stem"
version: 1.0.0
---

# repo-grand-oral-stem

> **GitHub 开源生态集成**: [epreuves-orales-bac/grand-oral-stem](https://github.com/epreuves-orales-bac/grand-oral-stem)
> 技术栈: `Markdown, PDF` | 业务领域: `France Bac`

## 1. 仓库定位与核心资产
针对法国高考大口试 (Grand Oral) 数理方向的选题库与答辩模板

- **官方仓库地址**: [https://github.com/epreuves-orales-bac/grand-oral-stem](https://github.com/epreuves-orales-bac/grand-oral-stem)
- **技术选型与实现**: `Markdown, PDF`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/epreuves-orales-bac/grand-oral-stem.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-grand-oral-stem --inspect-upstream
```
