from sqlalchemy.orm import Session
from datetime import datetime
from models.invoices.invoice_model import InvoiceLogDB


def create_invoice_log(db: Session, order_id: str, invoice_data: dict):
    db_log = InvoiceLogDB(
        order_id=order_id,
        invoice_data=invoice_data,
        submission_status="pending"
    )
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log


def update_invoice_log(db: Session, log_id: int, tax_response: dict, status: str):
    db_log = db.query(InvoiceLogDB).filter(InvoiceLogDB.id == log_id).first()
    if db_log:
        db_log.tax_authority_response = tax_response
        db_log.submission_status = status
        db_log.submitted_at = datetime.utcnow()
        db.commit()
        db.refresh(db_log)
    return db_log


def update_invoice_log_by_order_id(db: Session, order_id: str, tax_response: dict, status: str):
    db_log = db.query(InvoiceLogDB).filter(InvoiceLogDB.order_id == order_id).first()
    if db_log:
        db_log.tax_authority_response = tax_response
        db_log.submission_status = status
        db_log.submitted_at = datetime.utcnow()
        db.commit()
        db.refresh(db_log)
    return db_log


# Get invoice submission statistics
def get_invoice_stats(db: Session):
    total = db.query(InvoiceLogDB).count()
    submitted = db.query(InvoiceLogDB).filter(InvoiceLogDB.submission_status == "submitted").count()
    failed = db.query(InvoiceLogDB).filter(InvoiceLogDB.submission_status == "failed").count()
    pending = db.query(InvoiceLogDB).filter(InvoiceLogDB.submission_status == "pending").count()

    return {
        "total_invoices": total,
        "submitted": submitted,
        "failed": failed,
        "pending": pending,
        "success_rate": submitted / total if total > 0 else 0
    }


def create_invoice_log(db: Session, order_id: str, invoice_data: dict):
    db_log = InvoiceLogDB(
        order_id=order_id,
        invoice_data=invoice_data,
        submission_status="pending"
    )
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log

def update_invoice_log(db: Session, log_id: int, tax_response: dict, status: str):
    db_log = db.query(InvoiceLogDB).filter(InvoiceLogDB.id == log_id).first()
    if db_log:
        db_log.tax_authority_response = tax_response
        db_log.submission_status = status
        db_log.submitted_at = datetime.utcnow()
        db.commit()
        db.refresh(db_log)
    return db_log