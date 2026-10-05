---
name: repo-ielts-vocab-mindmap
description: "ielts-vocabulary-mindmap-visualizer/d3 - 雅思写作常考 10 大社会话题（环境/科技/教育/犯罪）词汇逻辑脑图"
category: github_ecosystem
repo: "ielts-vocabulary-mindmap-visualizer/d3"
tech_stack: "JavaScript, D3.js"
domain: "IELTS Vocab"
url: "https://github.com/ielts-vocabulary-mindmap-visualizer/d3"
version: 1.0.0
---

# repo-ielts-vocab-mindmap

> **GitHub 开源生态集成**: [ielts-vocabulary-mindmap-visualizer/d3](https://github.com/ielts-vocabulary-mindmap-visualizer/d3)
> 技术栈: `JavaScript, D3.js` | 业务领域: `IELTS Vocab`

## 1. 仓库定位与核心资产
雅思写作常考 10 大社会话题（环境/科技/教育/犯罪）词汇逻辑脑图

- **官方仓库地址**: [https://github.com/ielts-vocabulary-mindmap-visualizer/d3](https://github.com/ielts-vocabulary-mindmap-visualizer/d3)
- **技术选型与实现**: `JavaScript, D3.js`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/ielts-vocabulary-mindmap-visualizer/d3.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-ielts-vocab-mindmap --inspect-upstream
```
