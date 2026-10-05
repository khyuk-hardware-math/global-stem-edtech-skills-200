---
name: repo-korean-sat-llm-leaderboard
description: "Marker-Inc-Korea/Korean-SAT-LLM-Leaderboard - 使用韩国高考修能题目对前沿 LLM 推理能力测评权威榜单"
category: github_ecosystem
repo: "Marker-Inc-Korea/Korean-SAT-LLM-Leaderboard"
tech_stack: "Python, HuggingFace"
domain: "Korea CSAT"
url: "https://github.com/Marker-Inc-Korea/Korean-SAT-LLM-Leaderboard"
version: 1.0.0
---

# repo-korean-sat-llm-leaderboard

> **GitHub 开源生态集成**: [Marker-Inc-Korea/Korean-SAT-LLM-Leaderboard](https://github.com/Marker-Inc-Korea/Korean-SAT-LLM-Leaderboard)
> 技术栈: `Python, HuggingFace` | 业务领域: `Korea CSAT`

## 1. 仓库定位与核心资产
使用韩国高考修能题目对前沿 LLM 推理能力测评权威榜单

- **官方仓库地址**: [https://github.com/Marker-Inc-Korea/Korean-SAT-LLM-Leaderboard](https://github.com/Marker-Inc-Korea/Korean-SAT-LLM-Leaderboard)
- **技术选型与实现**: `Python, HuggingFace`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/Marker-Inc-Korea/Korean-SAT-LLM-Leaderboard.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-korean-sat-llm-leaderboard --inspect-upstream
```
