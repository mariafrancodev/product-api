from typing import List, Optional
from pydantic import BaseModel, Field


class PictureSchema(BaseModel):
    url: str
    size: Optional[str] = None


class SellerSchema(BaseModel):
    id: str
    name: Optional[str]


class ShippingSchema(BaseModel):
    free_shipping: bool
    logistic_type: Optional[str]


class AttributeSchema(BaseModel):
    name: str
    value: str


class ProductResponseSchema(BaseModel):
    id: str
    title: str
    price: float
    currency: str
    available_quantity: int
    sold_quantity: int
    condition: Optional[str]
    pictures: List[PictureSchema] = Field(default_factory=list)
    seller: Optional[SellerSchema]
    shipping: Optional[ShippingSchema]
    attributes: List[AttributeSchema] = Field(default_factory=list)

    class Config:
        orm_mode = True
