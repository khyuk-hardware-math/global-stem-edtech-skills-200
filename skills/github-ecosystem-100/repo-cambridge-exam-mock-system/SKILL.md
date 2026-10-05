---
name: repo-cambridge-exam-mock-system
description: "cambridge-exam-mock-system/lite - 轻量级 KET/PET 听力带音频时间轴与即时答卷测试系统"
category: github_ecosystem
repo: "cambridge-exam-mock-system/lite"
tech_stack: "React, Node.js"
domain: "Cambridge Mock"
url: "https://github.com/cambridge-exam-mock-system/lite"
version: 1.0.0
---

# repo-cambridge-exam-mock-system

> **GitHub 开源生态集成**: [cambridge-exam-mock-system/lite](https://github.com/cambridge-exam-mock-system/lite)
> 技术栈: `React, Node.js` | 业务领域: `Cambridge Mock`

## 1. 仓库定位与核心资产
轻量级 KET/PET 听力带音频时间轴与即时答卷测试系统

- **官方仓库地址**: [https://github.com/cambridge-exam-mock-system/lite](https://github.com/cambridge-exam-mock-system/lite)
- **技术选型与实现**: `React, Node.js`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/cambridge-exam-mock-system/lite.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-cambridge-exam-mock-system --inspect-upstream
```
