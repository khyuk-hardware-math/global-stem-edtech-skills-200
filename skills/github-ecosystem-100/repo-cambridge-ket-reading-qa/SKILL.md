---
name: repo-cambridge-ket-reading-qa
description: "cambridge-english-parser/ket-reading-qa - KET 阅读理解各题型（告示理解、单选、完形）自动化题干切片器"
category: github_ecosystem
repo: "cambridge-english-parser/ket-reading-qa"
tech_stack: "Python, Regex"
domain: "Cambridge KET"
url: "https://github.com/cambridge-english-parser/ket-reading-qa"
version: 1.0.0
---

# repo-cambridge-ket-reading-qa

> **GitHub 开源生态集成**: [cambridge-english-parser/ket-reading-qa](https://github.com/cambridge-english-parser/ket-reading-qa)
> 技术栈: `Python, Regex` | 业务领域: `Cambridge KET`

## 1. 仓库定位与核心资产
KET 阅读理解各题型（告示理解、单选、完形）自动化题干切片器

- **官方仓库地址**: [https://github.com/cambridge-english-parser/ket-reading-qa](https://github.com/cambridge-english-parser/ket-reading-qa)
- **技术选型与实现**: `Python, Regex`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/cambridge-english-parser/ket-reading-qa.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-cambridge-ket-reading-qa --inspect-upstream
```
