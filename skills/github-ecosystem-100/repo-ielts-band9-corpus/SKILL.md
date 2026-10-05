---
name: repo-ielts-band9-corpus
description: "ielts-band9-corpus/sample-essays - 收录数百篇前雅思考官认证的 Band 8.5-9.0 满分范文与精细批注库"
category: github_ecosystem
repo: "ielts-band9-corpus/sample-essays"
tech_stack: "Markdown, JSON"
domain: "IELTS Corpus"
url: "https://github.com/ielts-band9-corpus/sample-essays"
version: 1.0.0
---

# repo-ielts-band9-corpus

> **GitHub 开源生态集成**: [ielts-band9-corpus/sample-essays](https://github.com/ielts-band9-corpus/sample-essays)
> 技术栈: `Markdown, JSON` | 业务领域: `IELTS Corpus`

## 1. 仓库定位与核心资产
收录数百篇前雅思考官认证的 Band 8.5-9.0 满分范文与精细批注库

- **官方仓库地址**: [https://github.com/ielts-band9-corpus/sample-essays](https://github.com/ielts-band9-corpus/sample-essays)
- **技术选型与实现**: `Markdown, JSON`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/ielts-band9-corpus/sample-essays.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-ielts-band9-corpus --inspect-upstream
```
