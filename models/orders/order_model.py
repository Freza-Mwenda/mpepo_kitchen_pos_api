from sqlalchemy import Column, String, DateTime, JSON, DECIMAL
from datetime import datetime
from configs.database import Base


# SQLAlchemy Models for MySQL

class OrderDB(Base):
    __tablename__ = "orders"

    id = Column(String(50), primary_key=True, index=True)
    items = Column(JSON, nullable=False)  # Proper JSON type
    subtotal = Column(DECIMAL(10, 2), nullable=False)
    tax_amount = Column(DECIMAL(10, 2), nullable=False)
    discount_amount = Column(DECIMAL(10, 2), default=0.0)
    total = Column(DECIMAL(10, 2), nullable=False)
    status = Column(String(20), default="completed")
    created_at = Column(DateTime, default=datetime.utcnow)
    tax_authority_ref = Column(String(100), nullable=True)