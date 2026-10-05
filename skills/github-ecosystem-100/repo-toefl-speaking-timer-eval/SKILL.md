---
name: repo-toefl-speaking-timer-eval
description: "toefl-speaking-timer-eval/recorder - 精准呈现托福口语 15s 准备 / 45s 作答波形与倒计时的实战录音器"
category: github_ecosystem
repo: "toefl-speaking-timer-eval/recorder"
tech_stack: "TypeScript, Web Audio"
domain: "TOEFL Speaking"
url: "https://github.com/toefl-speaking-timer-eval/recorder"
version: 1.0.0
---

# repo-toefl-speaking-timer-eval

> **GitHub 开源生态集成**: [toefl-speaking-timer-eval/recorder](https://github.com/toefl-speaking-timer-eval/recorder)
> 技术栈: `TypeScript, Web Audio` | 业务领域: `TOEFL Speaking`

## 1. 仓库定位与核心资产
精准呈现托福口语 15s 准备 / 45s 作答波形与倒计时的实战录音器

- **官方仓库地址**: [https://github.com/toefl-speaking-timer-eval/recorder](https://github.com/toefl-speaking-timer-eval/recorder)
- **技术选型与实现**: `TypeScript, Web Audio`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/toefl-speaking-timer-eval/recorder.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-toefl-speaking-timer-eval --inspect-upstream
```
