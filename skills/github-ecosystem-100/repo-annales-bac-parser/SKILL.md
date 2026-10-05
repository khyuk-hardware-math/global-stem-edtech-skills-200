---
name: repo-annales-bac-parser
description: "annabac-project/annales-bac-parser - 法国 Bac 历年各科目真题 (Annales) 文本提取与题型分类器"
category: github_ecosystem
repo: "annabac-project/annales-bac-parser"
tech_stack: "Python, PDFMiner"
domain: "France Bac"
url: "https://github.com/annabac-project/annales-bac-parser"
version: 1.0.0
---

# repo-annales-bac-parser

> **GitHub 开源生态集成**: [annabac-project/annales-bac-parser](https://github.com/annabac-project/annales-bac-parser)
> 技术栈: `Python, PDFMiner` | 业务领域: `France Bac`

## 1. 仓库定位与核心资产
法国 Bac 历年各科目真题 (Annales) 文本提取与题型分类器

- **官方仓库地址**: [https://github.com/annabac-project/annales-bac-parser](https://github.com/annabac-project/annales-bac-parser)
- **技术选型与实现**: `Python, PDFMiner`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/annabac-project/annales-bac-parser.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-annales-bac-parser --inspect-upstream
```
