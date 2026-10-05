---
name: repo-haerae-kmmlu
description: "HAERAE-HUB/KMMLU - 包含大量韩国修能与专业等级考试题目的韩语多任务语言理解基准"
category: github_ecosystem
repo: "HAERAE-HUB/KMMLU"
tech_stack: "Python, Datasets"
domain: "Korea Benchmark"
url: "https://github.com/HAERAE-HUB/KMMLU"
version: 1.0.0
---

# repo-haerae-kmmlu

> **GitHub 开源生态集成**: [HAERAE-HUB/KMMLU](https://github.com/HAERAE-HUB/KMMLU)
> 技术栈: `Python, Datasets` | 业务领域: `Korea Benchmark`

## 1. 仓库定位与核心资产
包含大量韩国修能与专业等级考试题目的韩语多任务语言理解基准

- **官方仓库地址**: [https://github.com/HAERAE-HUB/KMMLU](https://github.com/HAERAE-HUB/KMMLU)
- **技术选型与实现**: `Python, Datasets`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/HAERAE-HUB/KMMLU.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-haerae-kmmlu --inspect-upstream
```
