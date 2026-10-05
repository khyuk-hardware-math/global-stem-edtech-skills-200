# -*- coding: utf-8 -*-
"""
core/fleet_executor.py
Hardware execution and compute node dispatcher adhering to IT Fleet specification.
"""

import os
import subprocess
from typing import Dict, Any

FLEET_NODES = {
    "seoul-m4-director": {
        "name": "Central Director (Korea)",
        "specs": "MacBook Pro 16\", M4 Pro 48GB RAM",
        "roles": ["Master Orchestrator", "Laya-MLX GPU Triage", "Gemma 4 12B Ollama", "Interactive Teacher"]
    },
    "gpu-cuda-node": {
        "name": "Heavy CUDA & Render Host (Korea)",
        "specs": "Ryzen 7 9800X3D, RTX 5070 12GB VRAM",
        "roles": ["Manim 3D Video Rendering", "YOLO Multimodal Handwriting OCR", "CUDA Heavy Inference"]
    },
    "storage-db-node": {
        "name": "High-Capacity Storage Node (Cluster Storage)",
        "specs": "Mac mini M2 Max, 32GB RAM, 4TB SSD",
        "roles": ["Large-Scale PYQ Vector DB", "Whisper Speech Scoring Server", "Docker Services"]
    },
    "edge-grading-node": {
        "name": "Edge AI & Grading Node (Regional Edge)",
        "specs": "Mac mini M4, 24GB RAM",
        "roles": ["Local K12 Auto-Grading Engine", "Offline Monitoring"]
    },
    "sync-backup-node": {
        "name": "Sync Hub & Backup Node (Global Gateway)",
        "specs": "Mac mini M1, 16GB RAM",
        "roles": ["Encrypted Mesh Sync Node", "Automated Mirror Gateway"]
    }
}

class FleetExecutor:
    def allocate_node(self, skill_meta: Dict[str, Any]) -> Dict[str, Any]:
        req_node = skill_meta.get("hardware_node", "seoul-m4-director")
        primary_key = "seoul-m4-director"
        if "gpu-cuda-node" in req_node:
            primary_key = "gpu-cuda-node"
        elif "storage-db-node" in req_node:
            primary_key = "storage-db-node"
        elif "edge-grading-node" in req_node:
            primary_key = "edge-grading-node"
            
        return {
            "selected_node": primary_key,
            "node_profile": FLEET_NODES.get(primary_key, FLEET_NODES["seoul-m4-director"]),
            "allocation_rationale": f"Selected based on workload matching for {skill_meta.get('id')}"
        }

if __name__ == "__main__":
    executor = FleetExecutor()
    alloc = executor.allocate_node({"id": "manim-3b1b-animation-director", "hardware_node": "seoul-m4-director / gpu-cuda-node"})
    print("Allocation result:", alloc)
