"""Application configuration."""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
PRODUCTS_FILE = DATA_DIR / "products.json"
