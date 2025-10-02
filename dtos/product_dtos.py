from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Dict, Any

# Pydantic Models for API

class ProductBase(BaseModel):
    name: str
    price: float
    category: str
    description: Optional[str] = None
    image_url: Optional[str] = None

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: str
    created_at: datetime

    class Config:
        from_attributes = True

class CartItem(BaseModel):
    product: Dict[str, Any]
    quantity: int