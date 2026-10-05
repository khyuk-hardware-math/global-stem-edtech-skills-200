---
name: repo-manim-community
description: "ManimCommunity/manim - 全球著名的数理教学动画引擎社区维护版，数学物理动态视频标杆"
category: github_ecosystem
repo: "ManimCommunity/manim"
tech_stack: "Python, FFmpeg, Cairo"
domain: "STEM Animation"
url: "https://github.com/ManimCommunity/manim"
version: 1.0.0
---

# repo-manim-community

> **GitHub 开源生态集成**: [ManimCommunity/manim](https://github.com/ManimCommunity/manim)
> 技术栈: `Python, FFmpeg, Cairo` | 业务领域: `STEM Animation`

## 1. 仓库定位与核心资产
全球著名的数理教学动画引擎社区维护版，数学物理动态视频标杆

- **官方仓库地址**: [https://github.com/ManimCommunity/manim](https://github.com/ManimCommunity/manim)
- **技术选型与实现**: `Python, FFmpeg, Cairo`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/ManimCommunity/manim.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-manim-community --inspect-upstream
```
