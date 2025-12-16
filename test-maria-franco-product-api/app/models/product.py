from typing import List, Optional
from pydantic import BaseModel, Field


class Picture(BaseModel):
    url: str
    size: Optional[str] = None


class Seller(BaseModel):
    id: str
    name: Optional[str]


class Shipping(BaseModel):
    free_shipping: bool
    logistic_type: Optional[str]


class Attribute(BaseModel):
    name: str
    value: str


class Product(BaseModel):
    id: str
    title: str
    price: float
    currency: str
    available_quantity: int
    sold_quantity: int
    condition: Optional[str]
    pictures: List[Picture] = Field(default_factory=list)
    seller: Optional[Seller]
    shipping: Optional[Shipping]
    attributes: List[Attribute] = Field(default_factory=list)
