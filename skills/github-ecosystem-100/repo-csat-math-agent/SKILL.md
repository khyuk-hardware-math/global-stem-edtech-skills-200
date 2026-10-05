---
name: repo-csat-math-agent
description: "2026-bwai-golang-korea/csat-math - 针对韩国修能微积分与几何大纲构建的解题代理后端与知识图谱"
category: github_ecosystem
repo: "2026-bwai-golang-korea/csat-math"
tech_stack: "Go, Gin, Redis"
domain: "Korea CSAT"
url: "https://github.com/2026-bwai-golang-korea/csat-math"
version: 1.0.0
---

# repo-csat-math-agent

> **GitHub 开源生态集成**: [2026-bwai-golang-korea/csat-math](https://github.com/2026-bwai-golang-korea/csat-math)
> 技术栈: `Go, Gin, Redis` | 业务领域: `Korea CSAT`

## 1. 仓库定位与核心资产
针对韩国修能微积分与几何大纲构建的解题代理后端与知识图谱

- **官方仓库地址**: [https://github.com/2026-bwai-golang-korea/csat-math](https://github.com/2026-bwai-golang-korea/csat-math)
- **技术选型与实现**: `Go, Gin, Redis`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/2026-bwai-golang-korea/csat-math.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-csat-math-agent --inspect-upstream
```
