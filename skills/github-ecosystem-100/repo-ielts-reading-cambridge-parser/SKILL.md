---
name: repo-ielts-reading-cambridge-parser
description: "ielts-reading-cambridge-parser/core - 剑桥雅思 4-19 历年阅读真题同义词替换字典自动提取器"
category: github_ecosystem
repo: "ielts-reading-cambridge-parser/core"
tech_stack: "Python, BeautifulSoup"
domain: "IELTS Reading"
url: "https://github.com/ielts-reading-cambridge-parser/core"
version: 1.0.0
---

# repo-ielts-reading-cambridge-parser

> **GitHub 开源生态集成**: [ielts-reading-cambridge-parser/core](https://github.com/ielts-reading-cambridge-parser/core)
> 技术栈: `Python, BeautifulSoup` | 业务领域: `IELTS Reading`

## 1. 仓库定位与核心资产
剑桥雅思 4-19 历年阅读真题同义词替换字典自动提取器

- **官方仓库地址**: [https://github.com/ielts-reading-cambridge-parser/core](https://github.com/ielts-reading-cambridge-parser/core)
- **技术选型与实现**: `Python, BeautifulSoup`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/ielts-reading-cambridge-parser/core.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-ielts-reading-cambridge-parser --inspect-upstream
```
