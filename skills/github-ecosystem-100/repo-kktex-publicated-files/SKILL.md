---
name: repo-kktex-publicated-files
description: "KKTeX/Publicated-Files - 专门用于还原日本大学入试模试与共通测试版面的 LaTeX 宏包库"
category: github_ecosystem
repo: "KKTeX/Publicated-Files"
tech_stack: "TeX / LaTeX"
domain: "Japan Common Test"
url: "https://github.com/KKTeX/Publicated-Files"
version: 1.0.0
---

# repo-kktex-publicated-files

> **GitHub 开源生态集成**: [KKTeX/Publicated-Files](https://github.com/KKTeX/Publicated-Files)
> 技术栈: `TeX / LaTeX` | 业务领域: `Japan Common Test`

## 1. 仓库定位与核心资产
专门用于还原日本大学入试模试与共通测试版面的 LaTeX 宏包库

- **官方仓库地址**: [https://github.com/KKTeX/Publicated-Files](https://github.com/KKTeX/Publicated-Files)
- **技术选型与实现**: `TeX / LaTeX`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/KKTeX/Publicated-Files.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-kktex-publicated-files --inspect-upstream
```
