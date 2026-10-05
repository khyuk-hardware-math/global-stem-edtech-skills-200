---
name: repo-deepseek-math
description: "deepseek-ai/DeepSeek-Math - 深度求索开源的数学专精模型，无需工具调用纯逻辑推导达国际一流"
category: github_ecosystem
repo: "deepseek-ai/DeepSeek-Math"
tech_stack: "Python, PyTorch"
domain: "Math Reasoning"
url: "https://github.com/deepseek-ai/DeepSeek-Math"
version: 1.0.0
---

# repo-deepseek-math

> **GitHub 开源生态集成**: [deepseek-ai/DeepSeek-Math](https://github.com/deepseek-ai/DeepSeek-Math)
> 技术栈: `Python, PyTorch` | 业务领域: `Math Reasoning`

## 1. 仓库定位与核心资产
深度求索开源的数学专精模型，无需工具调用纯逻辑推导达国际一流

- **官方仓库地址**: [https://github.com/deepseek-ai/DeepSeek-Math](https://github.com/deepseek-ai/DeepSeek-Math)
- **技术选型与实现**: `Python, PyTorch`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/deepseek-ai/DeepSeek-Math.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-deepseek-math --inspect-upstream
```
