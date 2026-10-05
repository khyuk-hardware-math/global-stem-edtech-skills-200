---
name: repo-gsm8k
description: "openai/grade-school-math - OpenAI 发布的经典小学与初中多步骤数理应用题推理数据集"
category: github_ecosystem
repo: "openai/grade-school-math"
tech_stack: "Python, JSONL"
domain: "Reasoning Dataset"
url: "https://github.com/openai/grade-school-math"
version: 1.0.0
---

# repo-gsm8k

> **GitHub 开源生态集成**: [openai/grade-school-math](https://github.com/openai/grade-school-math)
> 技术栈: `Python, JSONL` | 业务领域: `Reasoning Dataset`

## 1. 仓库定位与核心资产
OpenAI 发布的经典小学与初中多步骤数理应用题推理数据集

- **官方仓库地址**: [https://github.com/openai/grade-school-math](https://github.com/openai/grade-school-math)
- **技术选型与实现**: `Python, JSONL`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/openai/grade-school-math.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-gsm8k --inspect-upstream
```
