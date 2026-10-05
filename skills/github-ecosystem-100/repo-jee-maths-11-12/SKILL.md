---
name: repo-jee-maths-11-12
description: "Ratnesh-181998/jee-mathematics-11th-and-12th - 覆盖印度 11 与 12 年级全套对应 JEE 大纲的数学讲义与题型"
category: github_ecosystem
repo: "Ratnesh-181998/jee-mathematics-11th-and-12th"
tech_stack: "TeX, Markdown"
domain: "India JEE"
url: "https://github.com/Ratnesh-181998/jee-mathematics-11th-and-12th"
version: 1.0.0
---

# repo-jee-maths-11-12

> **GitHub 开源生态集成**: [Ratnesh-181998/jee-mathematics-11th-and-12th](https://github.com/Ratnesh-181998/jee-mathematics-11th-and-12th)
> 技术栈: `TeX, Markdown` | 业务领域: `India JEE`

## 1. 仓库定位与核心资产
覆盖印度 11 与 12 年级全套对应 JEE 大纲的数学讲义与题型

- **官方仓库地址**: [https://github.com/Ratnesh-181998/jee-mathematics-11th-and-12th](https://github.com/Ratnesh-181998/jee-mathematics-11th-and-12th)
- **技术选型与实现**: `TeX, Markdown`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/Ratnesh-181998/jee-mathematics-11th-and-12th.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-jee-maths-11-12 --inspect-upstream
```
