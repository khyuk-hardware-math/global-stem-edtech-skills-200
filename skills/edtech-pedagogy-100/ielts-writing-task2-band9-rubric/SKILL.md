---
name: ielts-writing-task2-band9-rubric
description: "雅思写作 Task 2 官方 4 维评分标准 (TR/CC/LR/GRA) 满分对标技能"
category: edtech_pedagogy
region: "IELTS Writing"
subject: "English"
hardware_node: "seoul-m4-director"
version: 1.0.0
---

# ielts-writing-task2-band9-rubric

> **雅思写作 Task 2 官方 4 维评分标准 (TR/CC/LR/GRA) 满分对标技能**
> 适用体系: `IELTS Writing` | 重点学科: `English` | 推荐算力: `seoul-m4-director`

## 1. 技能定位与核心价值
严格对照 4 维量表（TR, CC, LR, GRA）诊断，杜绝模版套话，强化论证深度与连贯衔接。

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
python3 -m core.dispatch_cli --skill ielts-writing-task2-band9-rubric --query "请生成一道该考点的进阶自适应测试题并给出解析"
```
