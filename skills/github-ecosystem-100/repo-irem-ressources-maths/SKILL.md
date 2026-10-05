---
name: repo-irem-ressources-maths
description: "irem-univ/irem-ressources-maths - 法国高等数学教育研究院 (IREM) 开放课程与教研案例集"
category: github_ecosystem
repo: "irem-univ/irem-ressources-maths"
tech_stack: "TeX, Markdown"
domain: "France Research"
url: "https://github.com/irem-univ/irem-ressources-maths"
version: 1.0.0
---

# repo-irem-ressources-maths

> **GitHub 开源生态集成**: [irem-univ/irem-ressources-maths](https://github.com/irem-univ/irem-ressources-maths)
> 技术栈: `TeX, Markdown` | 业务领域: `France Research`

## 1. 仓库定位与核心资产
法国高等数学教育研究院 (IREM) 开放课程与教研案例集

- **官方仓库地址**: [https://github.com/irem-univ/irem-ressources-maths](https://github.com/irem-univ/irem-ressources-maths)
- **技术选型与实现**: `TeX, Markdown`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/irem-univ/irem-ressources-maths.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-irem-ressources-maths --inspect-upstream
```
