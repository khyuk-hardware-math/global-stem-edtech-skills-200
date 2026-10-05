---
name: repo-moodle-qtype-stack
description: "maths/moodle-qtype_stack - 英国爱丁堡大学开发的基于 Maxima 代数系统的自动评估插件"
category: github_ecosystem
repo: "maths/moodle-qtype_stack"
tech_stack: "PHP, Maxima, Moodle"
domain: "A-Level / STEM"
url: "https://github.com/maths/moodle-qtype_stack"
version: 1.0.0
---

# repo-moodle-qtype-stack

> **GitHub 开源生态集成**: [maths/moodle-qtype_stack](https://github.com/maths/moodle-qtype_stack)
> 技术栈: `PHP, Maxima, Moodle` | 业务领域: `A-Level / STEM`

## 1. 仓库定位与核心资产
英国爱丁堡大学开发的基于 Maxima 代数系统的自动评估插件

- **官方仓库地址**: [https://github.com/maths/moodle-qtype_stack](https://github.com/maths/moodle-qtype_stack)
- **技术选型与实现**: `PHP, Maxima, Moodle`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/maths/moodle-qtype_stack.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-moodle-qtype-stack --inspect-upstream
```
