from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel, validator
from datetime import datetime
from typing import List, Optional
import json

from dtos.product_dtos import CartItem

# Pydantic Models for API

class OrderCreate(BaseModel):
    items: List[CartItem]
    subtotal: float
    tax_amount: float
    discount_amount: float = 0.0
    total: float


class Order(BaseModel):
    id: str
    items: List[CartItem]  # This should match the database JSON structure
    subtotal: float
    tax_amount: float
    discount_amount: float
    total: float
    status: str
    created_at: datetime
    tax_authority_ref: Optional[str] = None

    @validator('items', pre=True)
    def validate_items(cls, v):
        if isinstance(v, str):
            try:
                parsed_items = json.loads(v)
                # Ensure it's a list of CartItem compatible objects
                if isinstance(parsed_items, list):
                    return parsed_items
                else:
                    return []
            except json.JSONDecodeError:
                return []
        return v

    class Config:
        from_attributes = True