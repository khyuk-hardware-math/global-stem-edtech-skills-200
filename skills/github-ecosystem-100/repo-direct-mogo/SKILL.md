---
name: repo-direct-mogo
description: "Mangom72/Direct-mogo - 聚合 2006 年至今全部韩国高考修能、学评、模评真题 PDF 导出工具"
category: github_ecosystem
repo: "Mangom72/Direct-mogo"
tech_stack: "C#, .NET, WPF"
domain: "Korea CSAT"
url: "https://github.com/Mangom72/Direct-mogo"
version: 1.0.0
---

# repo-direct-mogo

> **GitHub 开源生态集成**: [Mangom72/Direct-mogo](https://github.com/Mangom72/Direct-mogo)
> 技术栈: `C#, .NET, WPF` | 业务领域: `Korea CSAT`

## 1. 仓库定位与核心资产
聚合 2006 年至今全部韩国高考修能、学评、模评真题 PDF 导出工具

- **官方仓库地址**: [https://github.com/Mangom72/Direct-mogo](https://github.com/Mangom72/Direct-mogo)
- **技术选型与实现**: `C#, .NET, WPF`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/Mangom72/Direct-mogo.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-direct-mogo --inspect-upstream
```
