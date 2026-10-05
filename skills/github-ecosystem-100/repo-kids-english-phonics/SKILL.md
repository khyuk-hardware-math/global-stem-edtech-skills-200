---
name: repo-kids-english-phonics
description: "kids-english-phonics-engine/web - 专为少儿英语设计的 44 个发音音标与自然拼读拆音练习交互组件"
category: github_ecosystem
repo: "kids-english-phonics-engine/web"
tech_stack: "JavaScript, Web Audio"
domain: "Kids Phonics"
url: "https://github.com/kids-english-phonics-engine/web"
version: 1.0.0
---

# repo-kids-english-phonics

> **GitHub 开源生态集成**: [kids-english-phonics-engine/web](https://github.com/kids-english-phonics-engine/web)
> 技术栈: `JavaScript, Web Audio` | 业务领域: `Kids Phonics`

## 1. 仓库定位与核心资产
专为少儿英语设计的 44 个发音音标与自然拼读拆音练习交互组件

- **官方仓库地址**: [https://github.com/kids-english-phonics-engine/web](https://github.com/kids-english-phonics-engine/web)
- **技术选型与实现**: `JavaScript, Web Audio`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/kids-english-phonics-engine/web.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-kids-english-phonics --inspect-upstream
```
