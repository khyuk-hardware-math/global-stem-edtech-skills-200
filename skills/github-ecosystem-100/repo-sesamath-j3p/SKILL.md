---
name: repo-sesamath-j3p
description: "sesamath/j3p - 法国 Sésamath 出品的个性化数学练习自适应路径引擎"
category: github_ecosystem
repo: "sesamath/j3p"
tech_stack: "JavaScript, HTML5, SVG"
domain: "France K-12"
url: "https://github.com/sesamath/j3p"
version: 1.0.0
---

# repo-sesamath-j3p

> **GitHub 开源生态集成**: [sesamath/j3p](https://github.com/sesamath/j3p)
> 技术栈: `JavaScript, HTML5, SVG` | 业务领域: `France K-12`

## 1. 仓库定位与核心资产
法国 Sésamath 出品的个性化数学练习自适应路径引擎

- **官方仓库地址**: [https://github.com/sesamath/j3p](https://github.com/sesamath/j3p)
- **技术选型与实现**: `JavaScript, HTML5, SVG`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/sesamath/j3p.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-sesamath-j3p --inspect-upstream
```
