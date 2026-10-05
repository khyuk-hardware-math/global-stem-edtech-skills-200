---
name: suken-math-certification-tutor
description: "日本实用数学技能检定 (数检) 1级/准1级 高等代数通关技能"
category: edtech_pedagogy
region: "Japan Suken"
subject: "Mathematics"
hardware_node: "seoul-m4-director"
version: 1.0.0
---

# suken-math-certification-tutor

> **日本实用数学技能检定 (数检) 1级/准1级 高等代数通关技能**
> 适用体系: `Japan Suken` | 重点学科: `Mathematics` | 推荐算力: `seoul-m4-director`

## 1. 技能定位与核心价值
覆盖数检 1 级、准 1 级与 2 级，针对微积分、线性代数和高等统计提供自适应通关评测。

## 2. 教学与解题策略契约 (Pedagogical Protocol)
- **输入参数校验**：接收题目题干（支持 LaTeX 数学公式、化学方程式、英语文本段落）、目标学生掌握层级与解题时间窗口。
- **苏格拉底步进引导 (Socratic Scaffolding)**：
  1. 状态空间与已知物理/几何/语法变量提炼；
  2. 识别核心认知冲突点或阻碍步骤；
  3. 分级启发式提示（Level 1 关键考点唤醒 -> Level 2 辅助线/守恒量/同义替换锁定 -> Level 3 形式化严密推导）；
  4. 最终输出采分点细化（Mark Scheme / 步骤得分）与常见易错陷阱警告。
- **排版标准**：数学与物理公式严格使用 KaTeX/LaTeX 标准语法，保证多行方程对齐（`aligned`），英语题型标注 CEFR/考官量表锚点。

## 3. 算力编排与硬件节点映射
- **主交互与逻辑推导**：`seoul-m4-director` (M4 Pro 48GB Unified RAM)
- **多模态图表/视觉解析**：`gpu-cuda-node` (RTX 5070 12GB CUDA 加速)
- **海量题库检索**：`storage-db-node` (4TB SSD 高速向量数据库)

## 4. 快速运行与测试指令
```bash
python3 -m core.dispatch_cli --skill suken-math-certification-tutor --query "请生成一道该考点的进阶自适应测试题并给出解析"
```
