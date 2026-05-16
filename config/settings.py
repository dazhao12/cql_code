"""Project-level runtime settings for CQL experiments."""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "raw_data.csv"
RESULT_DIR = BASE_DIR / "results"
MODEL_NAME = "cql_baseline"
NUM_EPOCHS = 5
BATCH_SIZE = 32
LEARNING_RATE = 1e-3
