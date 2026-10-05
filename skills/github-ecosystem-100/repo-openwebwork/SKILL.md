---
name: repo-openwebwork
description: "openwebwork/webwork2 - 美国数学协会 (MAA) 主导的数理开源在线作业与代数验证系统"
category: github_ecosystem
repo: "openwebwork/webwork2"
tech_stack: "Perl, C, MySQL"
domain: "Global Math"
url: "https://github.com/openwebwork/webwork2"
version: 1.0.0
---

# repo-openwebwork

> **GitHub 开源生态集成**: [openwebwork/webwork2](https://github.com/openwebwork/webwork2)
> 技术栈: `Perl, C, MySQL` | 业务领域: `Global Math`

## 1. 仓库定位与核心资产
美国数学协会 (MAA) 主导的数理开源在线作业与代数验证系统

- **官方仓库地址**: [https://github.com/openwebwork/webwork2](https://github.com/openwebwork/webwork2)
- **技术选型与实现**: `Perl, C, MySQL`

## 2. 真实接入与执行契约 (Integration & Execution Contract)
- **克隆与环境预热**:
  ```bash
  git clone --depth 1 https://github.com/openwebwork/webwork2.git
  ```
- **执行封装器接口**:
  - 该技能作为 K-skills router 的专科子工具，提供原生 Python 桥接，可直接加载题库数据、解析真题格式或调用求解器引擎。
- **算力节点编排**:
  - 运算型/模型型：派发至 `seoul-m4-director` (M4 Pro) 或 `gpu-cuda-node` (RTX 5070)
  - 存储与数据库：索引入 `storage-db-node` (4TB SSD)

## 3. CLI 调用指令
```bash
python3 -m core.dispatch_cli --skill repo-openwebwork --inspect-upstream
```
