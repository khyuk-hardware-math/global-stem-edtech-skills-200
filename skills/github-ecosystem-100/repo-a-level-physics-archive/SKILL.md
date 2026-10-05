---
name: repo-a-level-physics-archive
description: "A-Level-Physics-Archive/exam-papers - 英国 AQA, Edexcel, OCR 历年物理与数学大题数字化归档"
category: github_ecosystem
repo: "A-Level-Physics-Archive/exam-papers"
tech_stack: "TeX, Shell"
domain: "UK A-Level"
url: "https://github.com/A-Level-Physics-Archive/exam-papers"
version: 1.0.0
---

# repo-a-level-physics-archive

> **GitHub 开源生态集成**: [A-Level-Physics-Archive/exam-papers](https://github.com/A-Level-Physics-Archive/exam-papers)
> 技术栈: `TeX, Shell` | 业务领域: `UK A-Level`

## 1. 仓库定位与核心资产
英国 AQA, Edexcel, OCR 历年物理与数学大题数字化归档

- **官方仓库地址**: [https://github.com/A-Level-Physics-Archive/exam-papers](https://github.com/A-Level-Physics-Archive/exam-papers)
- **技术选型与实现**: `TeX, Shell`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/A-Level-Physics-Archive/exam-papers.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-a-level-physics-archive --inspect-upstream
```
