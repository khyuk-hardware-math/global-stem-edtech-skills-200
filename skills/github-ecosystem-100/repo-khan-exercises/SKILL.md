---
name: repo-khan-exercises
description: "Khan/khan-exercises - 可汗学院 (Khan Academy) 开源题目练习框架与全科题目库"
category: github_ecosystem
repo: "Khan/khan-exercises"
tech_stack: "JavaScript, Perseus"
domain: "Global K-12"
url: "https://github.com/Khan/khan-exercises"
version: 1.0.0
---

# repo-khan-exercises

> **GitHub 开源生态集成**: [Khan/khan-exercises](https://github.com/Khan/khan-exercises)
> 技术栈: `JavaScript, Perseus` | 业务领域: `Global K-12`

## 1. 仓库定位与核心资产
可汗学院 (Khan Academy) 开源题目练习框架与全科题目库

- **官方仓库地址**: [https://github.com/Khan/khan-exercises](https://github.com/Khan/khan-exercises)
- **技术选型与实现**: `JavaScript, Perseus`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/Khan/khan-exercises.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-khan-exercises --inspect-upstream
```
