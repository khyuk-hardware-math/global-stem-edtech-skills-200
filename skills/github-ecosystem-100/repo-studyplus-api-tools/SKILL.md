---
name: repo-studyplus-api-tools
description: "studyplus-api-tools/exam-tracker - 日本主流备考应用 Studyplus 的第三方学习时长与备考追踪工具"
category: github_ecosystem
repo: "studyplus-api-tools/exam-tracker"
tech_stack: "Python, TypeScript"
domain: "Japan Study"
url: "https://github.com/studyplus-api-tools/exam-tracker"
version: 1.0.0
---

# repo-studyplus-api-tools

> **GitHub 开源生态集成**: [studyplus-api-tools/exam-tracker](https://github.com/studyplus-api-tools/exam-tracker)
> 技术栈: `Python, TypeScript` | 业务领域: `Japan Study`

## 1. 仓库定位与核心资产
日本主流备考应用 Studyplus 的第三方学习时长与备考追踪工具

- **官方仓库地址**: [https://github.com/studyplus-api-tools/exam-tracker](https://github.com/studyplus-api-tools/exam-tracker)
- **技术选型与实现**: `Python, TypeScript`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/studyplus-api-tools/exam-tracker.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-studyplus-api-tools --inspect-upstream
```
