---
name: repo-ielts-writing-task1-data
description: "ielts-writing-task1-data-engine/src - 输入图表数值自动生成雅思学术 Task 1 标准客观描述句型代码库"
category: github_ecosystem
repo: "ielts-writing-task1-data-engine/src"
tech_stack: "Python, Matplotlib"
domain: "IELTS Writing"
url: "https://github.com/ielts-writing-task1-data-engine/src"
version: 1.0.0
---

# repo-ielts-writing-task1-data

> **GitHub 开源生态集成**: [ielts-writing-task1-data-engine/src](https://github.com/ielts-writing-task1-data-engine/src)
> 技术栈: `Python, Matplotlib` | 业务领域: `IELTS Writing`

## 1. 仓库定位与核心资产
输入图表数值自动生成雅思学术 Task 1 标准客观描述句型代码库

- **官方仓库地址**: [https://github.com/ielts-writing-task1-data-engine/src](https://github.com/ielts-writing-task1-data-engine/src)
- **技术选型与实现**: `Python, Matplotlib`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/ielts-writing-task1-data-engine/src.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-ielts-writing-task1-data --inspect-upstream
```
