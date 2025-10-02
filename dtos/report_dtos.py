from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from typing import List

from dtos.order_dtos import Order

# Pydantic Models for API

class DailySalesReport(BaseModel):
    date: str
    total_sales: float
    total_orders: int
    total_tax: float
    average_order_value: float
    orders: List[Order]

class TaxReport(BaseModel):
    period: str
    total_tax_collected: float
    total_invoices: int
    invoice_details: List[dict]