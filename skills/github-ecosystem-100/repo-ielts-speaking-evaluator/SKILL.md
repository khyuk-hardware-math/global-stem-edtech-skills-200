---
name: repo-ielts-speaking-evaluator
description: "ielts-speaking-evaluator/speech-rater - 基于 Whisper 语音识别与声学特征分析的雅思口语流利度评分工具"
category: github_ecosystem
repo: "ielts-speaking-evaluator/speech-rater"
tech_stack: "Python, Whisper, Librosa"
domain: "IELTS Speaking"
url: "https://github.com/ielts-speaking-evaluator/speech-rater"
version: 1.0.0
---

# repo-ielts-speaking-evaluator

> **GitHub 开源生态集成**: [ielts-speaking-evaluator/speech-rater](https://github.com/ielts-speaking-evaluator/speech-rater)
> 技术栈: `Python, Whisper, Librosa` | 业务领域: `IELTS Speaking`

## 1. 仓库定位与核心资产
基于 Whisper 语音识别与声学特征分析的雅思口语流利度评分工具

- **官方仓库地址**: [https://github.com/ielts-speaking-evaluator/speech-rater](https://github.com/ielts-speaking-evaluator/speech-rater)
- **技术选型与实现**: `Python, Whisper, Librosa`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/ielts-speaking-evaluator/speech-rater.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-ielts-speaking-evaluator --inspect-upstream
```
