---
name: repo-highschool-math-genkuroki
description: "genkuroki/HighSchoolMath - 东北大学黑木玄教授整理的日本高校数学与大学入试深度解析笔记"
category: github_ecosystem
repo: "genkuroki/HighSchoolMath"
tech_stack: "TeX, Jupyter, Julia"
domain: "Japan Math"
url: "https://github.com/genkuroki/HighSchoolMath"
version: 1.0.0
---

# repo-highschool-math-genkuroki

> **GitHub 开源生态集成**: [genkuroki/HighSchoolMath](https://github.com/genkuroki/HighSchoolMath)
> 技术栈: `TeX, Jupyter, Julia` | 业务领域: `Japan Math`

## 1. 仓库定位与核心资产
东北大学黑木玄教授整理的日本高校数学与大学入试深度解析笔记

- **官方仓库地址**: [https://github.com/genkuroki/HighSchoolMath](https://github.com/genkuroki/HighSchoolMath)
- **技术选型与实现**: `TeX, Jupyter, Julia`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/genkuroki/HighSchoolMath.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-highschool-math-genkuroki --inspect-upstream
```
