import json
from pathlib import Path
from typing import List, Optional

from app.models.product import Product

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "products.json"


def load_products() -> List[dict]:
    """Load all products from the JSON file."""
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_products(products: List[dict]) -> None:
    """Save the given product list to the JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(products, f, indent=4)


def get_all_products() -> List[dict]:
    """Return all products."""
    return load_products()


def get_product_by_id(product_id: int) -> Optional[dict]:
    """Return a single product by ID."""
    products = load_products()
    return next((p for p in products if p["id"] == product_id), None)


def create_product(product: Product) -> dict:
    """Create a new product."""
    products = load_products()
    products.append(product.dict())
    save_products(products)
    return product.dict()


def update_product(product_id: int, new_data: Product) -> Optional[dict]:
    """Update an existing product by ID."""
    products = load_products()
    for idx, p in enumerate(products):
        if p["id"] == str(product_id):
            products[idx] = new_data.dict()
            save_products(products)
            return new_data.dict()
    return None


def delete_product(product_id: int) -> bool:
    """Delete a product by ID."""
    products = load_products()
    new_products = [p for p in products if p["id"] != product_id]
    if len(new_products) == len(products):
        return False
    save_products(new_products)
    return True
