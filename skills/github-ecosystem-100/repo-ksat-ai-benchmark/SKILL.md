---
name: repo-ksat-ai-benchmark
description: "roboco-io/KSAT-AI-Benchmark - 韩国高考自动化题目解析、视觉图表处理与大模型自动做题评分流"
category: github_ecosystem
repo: "roboco-io/KSAT-AI-Benchmark"
tech_stack: "Python, FastAPI"
domain: "Korea CSAT"
url: "https://github.com/roboco-io/KSAT-AI-Benchmark"
version: 1.0.0
---

# repo-ksat-ai-benchmark

> **GitHub 开源生态集成**: [roboco-io/KSAT-AI-Benchmark](https://github.com/roboco-io/KSAT-AI-Benchmark)
> 技术栈: `Python, FastAPI` | 业务领域: `Korea CSAT`

## 1. 仓库定位与核心资产
韩国高考自动化题目解析、视觉图表处理与大模型自动做题评分流

- **官方仓库地址**: [https://github.com/roboco-io/KSAT-AI-Benchmark](https://github.com/roboco-io/KSAT-AI-Benchmark)
- **技术选型与实现**: `Python, FastAPI`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/roboco-io/KSAT-AI-Benchmark.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-ksat-ai-benchmark --inspect-upstream
```
