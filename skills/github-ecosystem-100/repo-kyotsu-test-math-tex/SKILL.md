---
name: repo-kyotsu-test-math-tex
description: "kyotsu-test-archive/math-papers-tex - 日本历年大学入试中心试验与共通测试数学真题 LaTeX 数字化归档"
category: github_ecosystem
repo: "kyotsu-test-archive/math-papers-tex"
tech_stack: "LaTeX, Shell"
domain: "Japan Common Test"
url: "https://github.com/kyotsu-test-archive/math-papers-tex"
version: 1.0.0
---

# repo-kyotsu-test-math-tex

> **GitHub 开源生态集成**: [kyotsu-test-archive/math-papers-tex](https://github.com/kyotsu-test-archive/math-papers-tex)
> 技术栈: `LaTeX, Shell` | 业务领域: `Japan Common Test`

## 1. 仓库定位与核心资产
日本历年大学入试中心试验与共通测试数学真题 LaTeX 数字化归档

- **官方仓库地址**: [https://github.com/kyotsu-test-archive/math-papers-tex](https://github.com/kyotsu-test-archive/math-papers-tex)
- **技术选型与实现**: `LaTeX, Shell`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/kyotsu-test-archive/math-papers-tex.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-kyotsu-test-math-tex --inspect-upstream
```
