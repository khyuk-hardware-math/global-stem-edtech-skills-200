---
name: repo-cbse-ncert-scrapers
description: "avinash-k/cbse-ncert-scrapers - 抓取与清洗印度 NCERT 官方 9-12 年级数理化教科书工具"
category: github_ecosystem
repo: "avinash-k/cbse-ncert-scrapers"
tech_stack: "Python, BeautifulSoup"
domain: "India CBSE"
url: "https://github.com/avinash-k/cbse-ncert-scrapers"
version: 1.0.0
---

# repo-cbse-ncert-scrapers

> **GitHub 开源生态集成**: [avinash-k/cbse-ncert-scrapers](https://github.com/avinash-k/cbse-ncert-scrapers)
> 技术栈: `Python, BeautifulSoup` | 业务领域: `India CBSE`

## 1. 仓库定位与核心资产
抓取与清洗印度 NCERT 官方 9-12 年级数理化教科书工具

- **官方仓库地址**: [https://github.com/avinash-k/cbse-ncert-scrapers](https://github.com/avinash-k/cbse-ncert-scrapers)
- **技术选型与实现**: `Python, BeautifulSoup`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/avinash-k/cbse-ncert-scrapers.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-cbse-ncert-scrapers --inspect-upstream
```
