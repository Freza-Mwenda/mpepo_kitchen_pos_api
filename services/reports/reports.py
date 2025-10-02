from sqlalchemy.orm import Session
from sqlalchemy import cast, Date
from datetime import datetime, timedelta
from decimal import Decimal

from models.orders.order_model import OrderDB


def get_daily_sales_report(db: Session, date: str = None):
    """Generate daily sales report for MySQL"""
    if not date:
        date = datetime.utcnow().date()
    else:
        date = datetime.strptime(date, "%Y-%m-%d").date()
    
    # Get orders for the specific date (MySQL compatible)
    orders = db.query(OrderDB).filter(
        cast(OrderDB.created_at, Date) == date
    ).all()
    
    total_sales = float(sum(Decimal(str(order.total)) for order in orders))
    total_orders = len(orders)
    total_tax = float(sum(Decimal(str(order.tax_amount)) for order in orders))
    average_order_value = total_sales / total_orders if total_orders > 0 else 0
    
    return {
        "date": date.strftime("%Y-%m-%d"),
        "total_sales": round(total_sales, 2),
        "total_orders": total_orders,
        "total_tax": round(total_tax, 2),
        "average_order_value": round(average_order_value, 2),
        "orders": [
            {
                "id": order.id,
                "total": float(order.total),
                "tax_amount": float(order.tax_amount),
                "created_at": order.created_at.isoformat(),
                "item_count": len(order.items) if order.items else 0
            }
            for order in orders
        ]
    }

def get_tax_report(db: Session, start_date: str, end_date: str):
    """Generate tax report for a period"""
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d") + timedelta(days=1)
    
    orders = db.query(OrderDB).filter(
        OrderDB.created_at >= start_date,
        OrderDB.created_at < end_date
    ).all()
    
    total_tax_collected = float(sum(Decimal(str(order.tax_amount)) for order in orders))
    
    invoice_details = []
    for order in orders:
        invoice_details.append({
            "order_id": order.id,
            "date": order.created_at.strftime("%Y-%m-%d"),
            "tax_amount": float(order.tax_amount),
            "total_amount": float(order.total),
            "tax_authority_ref": order.tax_authority_ref,
            "item_count": len(order.items) if order.items else 0
        })
    
    return {
        "period": f"{start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}",
        "total_tax_collected": round(total_tax_collected, 2),
        "total_invoices": len(orders),
        "invoice_details": invoice_details
    }

def get_sales_summary(db: Session, days: int = 30):
    """Get sales summary for the last N days"""
    end_date = datetime.utcnow()
    start_date = end_date - timedelta(days=days)
    
    orders = db.query(OrderDB).filter(
        OrderDB.created_at >= start_date,
        OrderDB.created_at <= end_date
    ).all()
    
    # Group orders by date (MySQL compatible)
    daily_data = {}
    current_date = start_date.date()
    while current_date <= end_date.date():
        daily_data[current_date.strftime("%Y-%m-%d")] = {
            "date": current_date.strftime("%Y-%m-%d"),
            "total_sales": 0.0,
            "order_count": 0,
            "total_tax": 0.0
        }
        current_date += timedelta(days=1)
    
    for order in orders:
        date_key = order.created_at.date().strftime("%Y-%m-%d")
        if date_key in daily_data:
            daily_data[date_key]["total_sales"] += float(order.total)
            daily_data[date_key]["order_count"] += 1
            daily_data[date_key]["total_tax"] += float(order.tax_amount)
    
    total_sales = float(sum(Decimal(str(order.total)) for order in orders))
    total_tax = float(sum(Decimal(str(order.tax_amount)) for order in orders))
    
    return {
        "period": f"Last {days} days",
        "total_sales": round(total_sales, 2),
        "total_orders": len(orders),
        "total_tax": round(total_tax, 2),
        "daily_breakdown": list(daily_data.values())
    }