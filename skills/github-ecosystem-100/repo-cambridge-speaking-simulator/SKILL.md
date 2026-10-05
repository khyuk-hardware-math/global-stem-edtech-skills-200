---
name: repo-cambridge-speaking-simulator
description: "cambridge-speaking-simulator/ws - 模拟剑桥 KET/PET 真实口语考试双考官与两位考生互动情境引擎"
category: github_ecosystem
repo: "cambridge-speaking-simulator/ws"
tech_stack: "Python, WebSocket"
domain: "Cambridge Speaking"
url: "https://github.com/cambridge-speaking-simulator/ws"
version: 1.0.0
---

# repo-cambridge-speaking-simulator

> **GitHub 开源生态集成**: [cambridge-speaking-simulator/ws](https://github.com/cambridge-speaking-simulator/ws)
> 技术栈: `Python, WebSocket` | 业务领域: `Cambridge Speaking`

## 1. 仓库定位与核心资产
模拟剑桥 KET/PET 真实口语考试双考官与两位考生互动情境引擎

- **官方仓库地址**: [https://github.com/cambridge-speaking-simulator/ws](https://github.com/cambridge-speaking-simulator/ws)
- **技术选型与实现**: `Python, WebSocket`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/cambridge-speaking-simulator/ws.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-cambridge-speaking-simulator --inspect-upstream
```
