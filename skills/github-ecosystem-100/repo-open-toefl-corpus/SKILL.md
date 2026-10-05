---
name: repo-open-toefl-corpus
description: "open-toefl-corpus/transcripts - 收录托福历年学术讲座（天文/地质/考古/生物）真实文本与生词释义"
category: github_ecosystem
repo: "open-toefl-corpus/transcripts"
tech_stack: "JSON, Markdown"
domain: "TOEFL Corpus"
url: "https://github.com/open-toefl-corpus/transcripts"
version: 1.0.0
---

# repo-open-toefl-corpus

> **GitHub 开源生态集成**: [open-toefl-corpus/transcripts](https://github.com/open-toefl-corpus/transcripts)
> 技术栈: `JSON, Markdown` | 业务领域: `TOEFL Corpus`

## 1. 仓库定位与核心资产
收录托福历年学术讲座（天文/地质/考古/生物）真实文本与生词释义

- **官方仓库地址**: [https://github.com/open-toefl-corpus/transcripts](https://github.com/open-toefl-corpus/transcripts)
- **技术选型与实现**: `JSON, Markdown`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/open-toefl-corpus/transcripts.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-open-toefl-corpus --inspect-upstream
```
