import json
from pathlib import Path

DATA_FILE=Path(__file__).parent / "mock_data.json"

with open(DATA_FILE, "r") as file:
    ORDERS_DB = json.load(file)    