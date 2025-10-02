from sqlalchemy import Column, Integer, String, DateTime, JSON
from datetime import datetime
from configs.database import Base


# SQLAlchemy Models for MySQL

class InvoiceLogDB(Base):
    __tablename__ = "invoice_logs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(String(50), nullable=False, index=True)
    invoice_data = Column(JSON, nullable=False)
    submission_status = Column(String(20), default="pending")
    tax_authority_response = Column(JSON, nullable=True)
    submitted_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)