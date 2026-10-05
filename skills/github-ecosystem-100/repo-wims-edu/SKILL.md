---
name: repo-wims-edu
description: "wimsedu/wims - 法国大学、预科 (CPGE) 与高中广泛使用的交互式多功能教学服务器"
category: github_ecosystem
repo: "wimsedu/wims"
tech_stack: "C, Shell, Perl, LaTeX"
domain: "France CPGE"
url: "https://github.com/wimsedu/wims"
version: 1.0.0
---

# repo-wims-edu

> **GitHub 开源生态集成**: [wimsedu/wims](https://github.com/wimsedu/wims)
> 技术栈: `C, Shell, Perl, LaTeX` | 业务领域: `France CPGE`

## 1. 仓库定位与核心资产
法国大学、预科 (CPGE) 与高中广泛使用的交互式多功能教学服务器

- **官方仓库地址**: [https://github.com/wimsedu/wims](https://github.com/wimsedu/wims)
- **技术选型与实现**: `C, Shell, Perl, LaTeX`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/wimsedu/wims.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-wims-edu --inspect-upstream
```
