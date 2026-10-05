---
name: repo-awesome-ielts-prep
description: "awesome-ielts-prep/curated-materials - 聚合全球高分雅思备考经验、剑桥真题解析与词汇替换表清单"
category: github_ecosystem
repo: "awesome-ielts-prep/curated-materials"
tech_stack: "Markdown"
domain: "IELTS Resources"
url: "https://github.com/awesome-ielts-prep/curated-materials"
version: 1.0.0
---

# repo-awesome-ielts-prep

> **GitHub 开源生态集成**: [awesome-ielts-prep/curated-materials](https://github.com/awesome-ielts-prep/curated-materials)
> 技术栈: `Markdown` | 业务领域: `IELTS Resources`

## 1. 仓库定位与核心资产
聚合全球高分雅思备考经验、剑桥真题解析与词汇替换表清单

- **官方仓库地址**: [https://github.com/awesome-ielts-prep/curated-materials](https://github.com/awesome-ielts-prep/curated-materials)
- **技术选型与实现**: `Markdown`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/awesome-ielts-prep/curated-materials.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-awesome-ielts-prep --inspect-upstream
```
