---
name: repo-ib-math-ia-templates
description: "ib-math-ia-templates/exploration-guide - 国际文凭 IB DP 数学 HL 内部评估 (IA) 格式标准与范文模板"
category: github_ecosystem
repo: "ib-math-ia-templates/exploration-guide"
tech_stack: "LaTeX, Markdown"
domain: "IB DP Math"
url: "https://github.com/ib-math-ia-templates/exploration-guide"
version: 1.0.0
---

# repo-ib-math-ia-templates

> **GitHub 开源生态集成**: [ib-math-ia-templates/exploration-guide](https://github.com/ib-math-ia-templates/exploration-guide)
> 技术栈: `LaTeX, Markdown` | 业务领域: `IB DP Math`

## 1. 仓库定位与核心资产
国际文凭 IB DP 数学 HL 内部评估 (IA) 格式标准与范文模板

- **官方仓库地址**: [https://github.com/ib-math-ia-templates/exploration-guide](https://github.com/ib-math-ia-templates/exploration-guide)
- **技术选型与实现**: `LaTeX, Markdown`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/ib-math-ia-templates/exploration-guide.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-ib-math-ia-templates --inspect-upstream
```
