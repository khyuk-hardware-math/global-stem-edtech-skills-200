# -*- coding: utf-8 -*-
"""
scripts/dispatch_cli.py
Unified Command-Line Interface for Global STEM & EdTech 200 Skills.
Supports searching, routing, listing, and inspecting skills.
"""

import os
import sys
import argparse
import json
from pathlib import Path

# Add project root to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core.router import GlobalStemEdtechRouter
from core.fleet_executor import FleetExecutor

def main():
    parser = argparse.ArgumentParser(description="Global STEM & EdTech 200 Skills Dispatcher")
    parser.add_argument("--query", "-q", type=str, help="Search or route a natural language query")
    parser.add_argument("--skill", "-s", type=str, help="Specify an exact skill name to inspect")
    parser.add_argument("--list", "-l", action="store_true", help="List all 200 skills")
    parser.add_argument("--json", "-j", action="store_true", help="Output in JSON format")
    parser.add_argument("--inspect-upstream", action="store_true", help="Display upstream repo details")
    args = parser.parse_args()

    router = GlobalStemEdtechRouter()
    executor = FleetExecutor()

    if args.list:
        if args.json:
            print(json.dumps(router.catalog, ensure_ascii=False, indent=2))
        else:
            print(f"\n=== Global STEM & EdTech 200 Skills Catalog (Total: {len(router.catalog)}) ===")
            print(f"{'#':<4} {'Type':<18} {'Skill ID':<38} {'Domain / Region':<22}")
            print("-" * 86)
            for idx, s in enumerate(router.catalog, 1):
                stype = s.get("type", "")
                sid = s.get("id", "")
                dom = s.get("domain", "") or s.get("region", "")
                print(f"{idx:<4} {stype:<18} {sid:<38} {dom:<22}")
        return

    if args.skill:
        matched = [s for s in router.catalog if s["id"] == args.skill]
        if not matched:
            print(f"Error: Skill '{args.skill}' not found.")
            sys.exit(1)
        skill_meta = matched[0]
        allocation = executor.allocate_node(skill_meta)
        output = {
            "skill": skill_meta,
            "fleet_allocation": allocation,
            "status": "ready"
        }
        if args.json:
            print(json.dumps(output, ensure_ascii=False, indent=2))
        else:
            print(f"\n[Skill Info]: {skill_meta['id']}")
            print(f"Title: {skill_meta.get('title')}")
            print(f"Type: {skill_meta.get('type')}")
            print(f"Description: {skill_meta.get('description')}")
            if "url" in skill_meta:
                print(f"Upstream URL: {skill_meta['url']}")
            print(f"Allocated Node: {allocation['selected_node']} ({allocation['node_profile']['name']})")
        return

    if args.query:
        matches = router.route_query(args.query, top_k=8)
        if args.json:
            print(json.dumps(matches, ensure_ascii=False, indent=2))
        else:
            print(f"\n=== Query Match Results for: '{args.query}' ===")
            for idx, item in enumerate(matches, 1):
                score = item["score"]
                s = item["skill"]
                print(f"{idx}. [{score:>5.1f} pts] {s['id']:<38} | {s.get('title')}")
        return

    parser.print_help()

if __name__ == "__main__":
    main()
