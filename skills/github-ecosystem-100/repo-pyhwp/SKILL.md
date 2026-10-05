---
name: repo-pyhwp
description: "pyhwp/pyhwp - 解析和转换韩国特有 HWP 格式考卷文档的开源核心库"
category: github_ecosystem
repo: "pyhwp/pyhwp"
tech_stack: "Python"
domain: "Korea Parser"
url: "https://github.com/pyhwp/pyhwp"
version: 1.0.0
---

# repo-pyhwp

> **GitHub 开源生态集成**: [pyhwp/pyhwp](https://github.com/pyhwp/pyhwp)
> 技术栈: `Python` | 业务领域: `Korea Parser`

## 1. 仓库定位与核心资产
解析和转换韩国特有 HWP 格式考卷文档的开源核心库

- **官方仓库地址**: [https://github.com/pyhwp/pyhwp](https://github.com/pyhwp/pyhwp)
- **技术选型与实现**: `Python`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/pyhwp/pyhwp.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-pyhwp --inspect-upstream
```
