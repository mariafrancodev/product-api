from typing import List

from fastapi import APIRouter, HTTPException

from app.models.product import Product
from app.services import product_service

router = APIRouter(prefix="/products", tags=["Products"])


@router.get("/", response_model=List[Product])
def get_products():
    """Return all products."""
    return product_service.get_all_products()


@router.get("/{product_id}", response_model=Product)
def get_product(product_id: int):
    """Return a single product by ID."""
    product = product_service.get_product_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.post("/", response_model=Product, status_code=201)
def create_product(product: Product):
    """Create a new product."""
    return product_service.create_product(product)


@router.put("/{product_id}", response_model=Product)
def update_product(product_id: int, product: Product):
    """Update an existing product by ID."""
    updated = product_service.update_product(product_id, product)
    if not updated:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated


@router.delete("/{product_id}", status_code=204)
def delete_product(product_id: int):
    """Delete a product by ID."""
    deleted = product_service.delete_product(product_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Product not found")
    return None
