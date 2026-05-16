"""
v1.0 - Baseline 训练脚本
基于：无
改动：初始化项目
"""
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from core.data_loader import load_medical_data

def main():
    data = load_medical_data("../Data/raw_data.csv")
    print("Starting CQL (Conservative Q-Learning) training baseline...")
    # 模拟模型训练逻辑
    print("Training complete. Saving results to ../Results/")

if __name__ == "__main__":
    main()
