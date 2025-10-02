from datetime import datetime
from typing import Optional
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from configs.database import get_db
from models.invoices.invoice_model import InvoiceLogDB
from services.invoices.invoice_service import get_invoice_stats
from services.reports.reports import get_daily_sales_report, get_tax_report, get_sales_summary

router = APIRouter()

# Reporting endpoints
@router.get("/daily-sales")
def get_daily_sales_report_endpoint(date: Optional[str] = None, db: Session = Depends(get_db)):
    return get_daily_sales_report(db, date)


@router.get("/tax-report")
def get_tax_report_endpoint(start_date: str, end_date: str, db: Session = Depends(get_db)):
    return get_tax_report(db, start_date, end_date)


@router.get("/sales-summary")
def get_sales_summary_endpoint(days: int = 30, db: Session = Depends(get_db)):
    return get_sales_summary(db, days)


# Tax submission reports endpoint
@router.get("/tax-submissions")
def get_tax_submission_report(db: Session = Depends(get_db)):
    """Get tax submission statistics and details"""
    stats = get_invoice_stats(db)

    # Get recent invoice logs
    recent_logs = db.query(InvoiceLogDB).order_by(InvoiceLogDB.created_at.desc()).limit(50).all()

    submission_details = []
    for log in recent_logs:
        submission_details.append({
            "order_id": log.order_id,
            "status": log.submission_status,
            "submitted_at": log.submitted_at.isoformat() if log.submitted_at else None,
            "authority_reference": log.tax_authority_response.get(
                "authority_reference") if log.tax_authority_response else None,
            "error_message": log.tax_authority_response.get("error_message") if log.tax_authority_response else None,
        })

    return {
        "statistics": stats,
        "recent_submissions": submission_details,
        "report_generated_at": datetime.utcnow().isoformat()
    }