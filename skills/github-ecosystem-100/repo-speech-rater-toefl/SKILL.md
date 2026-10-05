---
name: repo-speech-rater-toefl
description: "speech-rater-toefl/pronunciation-check - 模拟 ETS SpeechRater 对发音、语速波动与音节重音的客观评定"
category: github_ecosystem
repo: "speech-rater-toefl/pronunciation-check"
tech_stack: "Python, PyTorch, Kaldi"
domain: "TOEFL Speaking"
url: "https://github.com/speech-rater-toefl/pronunciation-check"
version: 1.0.0
---

# repo-speech-rater-toefl

> **GitHub 开源生态集成**: [speech-rater-toefl/pronunciation-check](https://github.com/speech-rater-toefl/pronunciation-check)
> 技术栈: `Python, PyTorch, Kaldi` | 业务领域: `TOEFL Speaking`

## 1. 仓库定位与核心资产
模拟 ETS SpeechRater 对发音、语速波动与音节重音的客观评定

- **官方仓库地址**: [https://github.com/speech-rater-toefl/pronunciation-check](https://github.com/speech-rater-toefl/pronunciation-check)
- **技术选型与实现**: `Python, PyTorch, Kaldi`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/speech-rater-toefl/pronunciation-check.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-speech-rater-toefl --inspect-upstream
```
