---
name: repo-toefl-vocab-flashcards
description: "toefl-vocabulary-flashcards-app/flutter - 集成托福高频 400 核心词、绿色词本与词根助记的移动端卡片程序"
category: github_ecosystem
repo: "toefl-vocabulary-flashcards-app/flutter"
tech_stack: "Flutter, Dart"
domain: "TOEFL Vocab"
url: "https://github.com/toefl-vocabulary-flashcards-app/flutter"
version: 1.0.0
---

# repo-toefl-vocab-flashcards

> **GitHub 开源生态集成**: [toefl-vocabulary-flashcards-app/flutter](https://github.com/toefl-vocabulary-flashcards-app/flutter)
> 技术栈: `Flutter, Dart` | 业务领域: `TOEFL Vocab`

## 1. 仓库定位与核心资产
集成托福高频 400 核心词、绿色词本与词根助记的移动端卡片程序

- **官方仓库地址**: [https://github.com/toefl-vocabulary-flashcards-app/flutter](https://github.com/toefl-vocabulary-flashcards-app/flutter)
- **技术选型与实现**: `Flutter, Dart`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/toefl-vocabulary-flashcards-app/flutter.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-toefl-vocab-flashcards --inspect-upstream
```
