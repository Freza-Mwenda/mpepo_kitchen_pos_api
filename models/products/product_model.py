from sqlalchemy import Column, Integer, String, DateTime, Text, DECIMAL
from datetime import datetime
from configs.database import Base


# SQLAlchemy Models for MySQL
class ProductDB(Base):
    __tablename__ = "products"

    id = Column(String(50), primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)
    category = Column(String(50), nullable=False)
    description = Column(Text, nullable=True)
    image_url = Column(String(10000), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Integer, default=1)