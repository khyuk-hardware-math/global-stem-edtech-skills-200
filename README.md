# Global STEM & EdTech 200 Skills (全球数理化教培与外语考培 200 专科技能库)

[![GitHub Actions CI](https://github.com/khyuk-hardware-math/global-stem-edtech-skills-200/actions/workflows/ci.yml/badge.svg)](https://github.com/khyuk-hardware-math/global-stem-edtech-skills-200/actions)
[![Skills Count](https://img.shields.io/badge/skills-200%20verified-blue)](core/catalog.json)
[![GitHub Stars](https://img.shields.io/github/stars/khyuk-hardware-math/global-stem-edtech-skills-200?style=social)](https://github.com/khyuk-hardware-math/global-stem-edtech-skills-200)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Orchestrator](https://img.shields.io/badge/K--Router-Compatible-purple)](https://github.com/khyuk-hardware-math/global-stem-edtech-skills-200)

> **专为严谨 STEM 教育、国际名校升学大考与标准化语言测评打造的 200 个高精度 Agent Skills 与开源工具库。**
> 严格恪守边界：全库仅聚焦 **100 个数理外语专科教学技能 (EdTech Pedagogy)** 与 **100 个顶尖 GitHub 开源数理基准/题库生态 (GitHub Ecosystem)**。

⭐ **如果你觉得这个项目对你的教研、解题、评测或 AI Agent 开发有所帮助，欢迎在右上角点击 Star 支持！**

---

## 🏛️ 架构全景与目录边界 (Architectural Layout)

```
global-stem-edtech-skills-200/
├── .github/
│   └── workflows/ci.yml              # GitHub Actions 自动化 CI 质量门禁流水线
├── core/
│   ├── catalog.json                  # 200 个技能强类型元数据总表 (类型/考纲/学科/推荐算力)
│   ├── router.py                     # 毫秒级语义与关键词匹配路由中枢
│   ├── fleet_executor.py             # 真实分布式机队算力分配器 (seoul-m4-director/gpu-cuda-node/storage-db-node/edge-grading-node/sync-backup-node)
│   └── asset_loader.py               # 真实可执行资产验证器 (SymPy / 雅思词汇密度 / 大纲库)
├── skills/
│   ├── edtech-pedagogy-100/          # [100 专科教学技能] 覆盖印/法/日/韩/美/英/澳与语言考培
│   │   ├── jee-advanced-rotational-dynamics/   (印度 JEE 高难刚体转动动力学)
│   │   ├── bac-maths-specialite-evaluator/     (法国 Bac 导数与空间向量)
│   │   ├── kyotsu-test-math-1a-speed/          (日本共通测试数学ⅠA限速推演)
│   │   ├── suneung-math-killer-22-30/          (韩国修能 22/30 杀手题微积分)
│   │   ├── ielts-writing-task2-band9-rubric/   (雅思写作 Task 2 官方 4 维量表)
│   │   └── ... (共 100 个独立文件夹，均含规范 SKILL.md 与 metadata.json)
│   └── github-ecosystem-100/         # [100 GitHub 开源生态包装器]
│       ├── repo-jeebench/                      (IIT Delhi JEE Advanced 评测基准)
│       ├── repo-coopmaths-mathalea/            (法国教育部官方数学变参题库)
│       ├── repo-kktex-publicated-files/        (日本入试/共通测试 LaTeX 考卷宏包)
│       ├── repo-direct-mogo/                   (韩国 20 年修能全套真题导出器)
│       ├── repo-manim-community/               (全球数学动画引擎 3B1B 社区版)
│       └── ... (共 100 个开源项目标准接入包装器)
├── scripts/
│   ├── dispatch_cli.py               # 统一命令行调度、查询与执行入口
│   └── sync_to_github.sh             # 一键向 GitHub 仓库提交与推送脚本
├── tests/
│   └── test_skills_integrity.py      # 自动化单元测试与 200 技能完整性校验套件
├── LICENSE                           # MIT 开源许可证
└── README.md
```

---

## 🌍 覆盖国家体系与考试方向

1. **印度 (India - 核心攻坚)**：JEE Main, JEE Advanced (物理/化学/数学), NEET (生物/物理/化学), CBSE/ICSE Board 9-12 年级大纲。
2. **法国 (France)**：Baccalauréat (Spécialité Mathématiques, Physique-Chimie), Collège 6e-3e (Brevet DNB), Lycée 2nde-Terminale, CPGE 高等预科 (MPSI/PCSI), Grand Oral 大口试。
3. **日本 (Japan)**：大学入学共通テスト (数学ⅠA/ⅡBC, 物理, 化学), 东大/京大等国立名校二次试验论述数学与理科, emath 考卷排版。
4. **韩国 (Korea)**：大学修学能力试验 (CSAT / 수능) 数学 22/30 杀手题 (Killer problems), 微积分/几何选考, 科学探究物理Ⅱ/化学Ⅱ, EBS 教材联动。
5. **英美澳国际学程**：美国 AP (Calculus BC, Physics C, Chemistry), 英国 A-Level (Further Maths, STEP, MAT), 澳大利亚 VCE/HSC (Specialist Maths), 全球数学竞赛 (AMC 10/12, AIME)。
6. **英语等级与出国大考**：剑桥五级英语 A2 Key (KET), B1 Preliminary (PET), 雅思 (IELTS Academic & General), 托福 (TOEFL iBT 新版学术讨论与长讲座精听)。
7. **数理动效与公式排版**：3Blue1Brown Manim, GeoGebra 动态几何, PhET 虚拟仿真, LaTeX/KaTeX/Typst 出版级考卷排版。

---

## ⚡ 快速开始 (Quickstart)

### 1. 克隆与检索
```bash
git clone https://github.com/khyuk-hardware-math/global-stem-edtech-skills-200.git
cd global-stem-edtech-skills-200

# 搜索印度 JEE 物理相关的技能与仓库
python3 scripts/dispatch_cli.py --query "印度 JEE 刚体动力学"

# 搜索法国高考数学生成器
python3 scripts/dispatch_cli.py --query "法国 Bac 数学 导数"

# 搜索雅思写作评分技能
python3 scripts/dispatch_cli.py --query "雅思 写作 Task 2 评分"
```

### 2. 查看特定技能详情与算力分配
```bash
python3 scripts/dispatch_cli.py --skill jee-advanced-rotational-dynamics
python3 scripts/dispatch_cli.py --skill repo-jeebench
```

### 3. 列出全库 200 个技能
```bash
python3 scripts/dispatch_cli.py --list
```

### 4. 运行全套自动化测试
```bash
python3 -m unittest discover -s tests -p "test_*.py"
```

---

## 🔗 K-Skills Router 调度对接

本仓库专为配合 `k-skills-router` (Omni-MDT Universal Router) 调度设计。K-Router 调度中枢会自动通过 `MDTSkillMatcher` 识别用户主诉，并在意图命中时无缝挂载此 200 专科技能。
