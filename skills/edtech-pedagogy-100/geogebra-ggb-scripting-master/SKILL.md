---
name: geogebra-ggb-scripting-master
description: "GeoGebra 动态几何、二次曲线轨迹与 3D 多面体投影构建技能"
category: edtech_pedagogy
region: "Interactive Math"
subject: "Geometry"
hardware_node: "seoul-m4-director"
version: 1.0.0
---

# geogebra-ggb-scripting-master

> **GeoGebra 动态几何、二次曲线轨迹与 3D 多面体投影构建技能**
> 适用体系: `Interactive Math` | 重点学科: `Geometry` | 推荐算力: `seoul-m4-director`

## 1. 技能定位与核心价值
自动化编写 GeoGebra 指令，生成滑块联动参数图形、圆锥曲线轨迹与三维多面体投影。

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
python3 -m core.dispatch_cli --skill geogebra-ggb-scripting-master --query "请生成一道该考点的进阶自适应测试题并给出解析"
```
