---
name: repo-anki-cambridge-english
description: "anki-cambridge-english/a2-b1-deck - 针对 KET/PET 考生的 Anki 记忆卡片组，配真人发音与例句"
category: github_ecosystem
repo: "anki-cambridge-english/a2-b1-deck"
tech_stack: "Python, Anki Deck"
domain: "Cambridge English"
url: "https://github.com/anki-cambridge-english/a2-b1-deck"
version: 1.0.0
---

# repo-anki-cambridge-english

> **GitHub 开源生态集成**: [anki-cambridge-english/a2-b1-deck](https://github.com/anki-cambridge-english/a2-b1-deck)
> 技术栈: `Python, Anki Deck` | 业务领域: `Cambridge English`

## 1. 仓库定位与核心资产
针对 KET/PET 考生的 Anki 记忆卡片组，配真人发音与例句

- **官方仓库地址**: [https://github.com/anki-cambridge-english/a2-b1-deck](https://github.com/anki-cambridge-english/a2-b1-deck)
- **技术选型与实现**: `Python, Anki Deck`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/anki-cambridge-english/a2-b1-deck.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-anki-cambridge-english --inspect-upstream
```
