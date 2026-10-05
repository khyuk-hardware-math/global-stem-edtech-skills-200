# -*- coding: utf-8 -*-
"""
tests/test_skills_integrity.py
Automated integrity test suite for Global STEM & EdTech 200 Skills.
Verifies skill directory structure, SKILL.md existence, JSON validity, and router behavior.
"""

import unittest
import json
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from core.router import GlobalStemEdtechRouter
from core.fleet_executor import FleetExecutor
from core.asset_loader import RealAssetLoader

class TestSkillsIntegrity(unittest.TestCase):
    def setUp(self):
        self.router = GlobalStemEdtechRouter()
        self.executor = FleetExecutor()

    def test_total_skill_count(self):
        self.assertEqual(len(self.router.catalog), 200, "Must contain exactly 200 skills.")
        edtech_count = sum(1 for s in self.router.catalog if s["type"] == "edtech_pedagogy")
        github_count = sum(1 for s in self.router.catalog if s["type"] == "github_ecosystem")
        self.assertEqual(edtech_count, 100, "Must contain exactly 100 EdTech pedagogy skills.")
        self.assertEqual(github_count, 100, "Must contain exactly 100 GitHub ecosystem skills.")

    def test_all_skill_md_files_exist(self):
        for s in self.router.catalog:
            p = REPO_ROOT / s["path"] / "SKILL.md"
            self.assertTrue(p.exists(), f"SKILL.md missing for {s['id']} at {p}")
            content = p.read_text(encoding="utf-8")
            self.assertTrue(content.startswith("---"), f"SKILL.md must contain frontmatter for {s['id']}")
            self.assertIn("name:", content)
            self.assertIn("description:", content)

    def test_routing_precision(self):
        # 1. India JEE query
        res_jee = self.router.route_query("印度 JEE 旋转动力学 物理")
        self.assertTrue(len(res_jee) > 0)
        self.assertIn("jee", res_jee[0]["skill"]["id"])

        # 2. France Bac query
        res_bac = self.router.route_query("法国 高考 Baccalauréat 数学 几何")
        self.assertTrue(len(res_bac) > 0)
        self.assertTrue("bac" in res_bac[0]["skill"]["id"] or "france" in res_bac[0]["skill"]["id"] or "mathalea" in res_bac[0]["skill"]["id"])

        # 3. Korea Suneung query
        res_suneung = self.router.route_query("韩国 高考 修能 22번 30번 killer 微积分")
        self.assertTrue(len(res_suneung) > 0)
        self.assertTrue("suneung" in res_suneung[0]["skill"]["id"] or "csat" in res_suneung[0]["skill"]["id"])

        # 4. IELTS query
        res_ielts = self.router.route_query("雅思 写作 Task 2 Band 9 评分")
        self.assertTrue(len(res_ielts) > 0)
        self.assertIn("ielts", res_ielts[0]["skill"]["id"])

    def test_fleet_allocation(self):
        alloc = self.executor.allocate_node({"id": "manim-3b1b-animation-director", "hardware_node": "seoul-m4-director / gpu-cuda-node"})
        self.assertIn(alloc["selected_node"], ["seoul-m4-director", "gpu-cuda-node"])

    def test_asset_loader(self):
        metrics = RealAssetLoader.evaluate_ielts_essay_metrics("This is an essay written for IELTS examination test purposes.")
        self.assertGreater(metrics["word_count"], 0)

if __name__ == "__main__":
    unittest.main()
