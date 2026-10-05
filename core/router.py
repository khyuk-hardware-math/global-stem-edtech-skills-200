# -*- coding: utf-8 -*-
"""
core/router.py
High-speed routing and dispatcher for Global STEM & EdTech 200 Skills.
Sub-millisecond intent categorization and scoring.
"""

import os
import json
import re
from pathlib import Path
from typing import Dict, Any, List

CATALOG_PATH = Path(__file__).resolve().parent / "catalog.json"

class GlobalStemEdtechRouter:
    def __init__(self):
        with open(CATALOG_PATH, "r", encoding="utf-8") as f:
            self.catalog = json.load(f)["skills"]

    def route_query(self, query: str, top_k: int = 5) -> List[Dict[str, Any]]:
        q_lower = query.lower()
        scored = []
        
        # Token extraction
        tokens = set(re.findall(r'[a-zA-Z0-9_-]{2,}', q_lower))
        cn_chunks = re.findall(r'[一-龥]+', query)
        for chunk in cn_chunks:
            for n in (2, 3, 4):
                for i in range(len(chunk) - n + 1):
                    tokens.add(chunk[i:i+n])

        # Synonyms & alias weights
        synonyms = {
            "jee": ["rotational", "irodov", "inorganic", "organic", "jeebench", "pyq", "kota", "ncert"],
            "印度": ["jee", "neet", "irodov", "ncert", "kota"],
            "bac": ["baccalaureat", "specialite", "titration", "lycee", "college", "sesamath", "mathalea", "wims"],
            "法国": ["bac", "college", "lycee", "sesamath", "mathalea", "wims", "cpge"],
            "共通测试": ["kyotsu", "1a", "2bc", "emath", "suken", "todai", "kyodai"],
            "日本": ["kyotsu", "todai", "kyodai", "emath", "suken", "butsuri"],
            "修能": ["suneung", "csat", "killer", "ebs", "hwp", "mogo"],
            "韩国": ["suneung", "csat", "ebs", "hwp", "killer"],
            "ket": ["a2", "cambridge", "phonics", "junior"],
            "pet": ["b1", "cambridge", "paraphrase", "email"],
            "雅思": ["ielts", "band9", "task1", "task2", "speaking", "reading", "listening"],
            "托福": ["toefl", "tpo", "speechrater", "awl", "discussion"],
            "数学": ["math", "calculus", "geometry", "algebra", "manim", "geogebra", "sympy"],
            "物理": ["physics", "dynamics", "circuit", "phet", "oscillation"],
            "化学": ["chemistry", "organic", "inorganic", "titration", "chemfig"]
        }

        expanded_tokens = set(tokens)
        for t in list(tokens):
            if t in synonyms:
                expanded_tokens.update(synonyms[t])

        for s in self.catalog:
            score = 0.0
            s_id = s["id"].lower()
            s_title = s.get("title", "").lower()
            s_desc = s.get("description", "").lower()
            s_domain = s.get("domain", "").lower() + " " + s.get("region", "").lower() + " " + s.get("subject", "").lower()

            for token in expanded_tokens:
                if token in s_id:
                    score += 10.0 if len(token) >= 3 else 5.0
                elif token in s_title:
                    score += 6.0
                elif token in s_domain:
                    score += 4.0
                elif token in s_desc:
                    score += 2.0

            if score > 0:
                scored.append({"score": round(score, 2), "skill": s})

        scored.sort(key=lambda x: x["score"], reverse=True)
        return scored[:top_k]

if __name__ == "__main__":
    router = GlobalStemEdtechRouter()
    res = router.route_query("印度 JEE 物理 旋转动力学")
    print(f"Query matched {len(res)} results:")
    for r in res:
        print(f"[{r['score']}] {r['skill']['id']} -> {r['skill']['title']}")
