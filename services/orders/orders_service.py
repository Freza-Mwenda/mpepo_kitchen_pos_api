from sqlalchemy.orm import Session
import uuid
from decimal import Decimal
import json
from models.orders.order_model import OrderDB


# Order CRUD functions
def create_order(db: Session, order_data: dict):
    # Ensure items are properly formatted as JSON-compatible objects
    items_data = order_data["items"]

    # Convert to JSON-serializable format if needed
    if isinstance(items_data, list):
        # Ensure each item is JSON serializable
        serializable_items = []
        for item in items_data:
            if hasattr(item, 'dict'):
                serializable_items.append(item.dict())
            else:
                serializable_items.append(item)
        items_data = serializable_items

    db_order = OrderDB(
        id=str(uuid.uuid4()),
        items=items_data,  # Store as proper JSON
        subtotal=Decimal(str(order_data["subtotal"])),
        tax_amount=Decimal(str(order_data["tax_amount"])),
        discount_amount=Decimal(str(order_data.get("discount_amount", 0.0))),
        total=Decimal(str(order_data["total"])),
        status="completed"
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


def get_orders(db: Session, skip: int = 0, limit: int = 100):
    orders = db.query(OrderDB).order_by(OrderDB.created_at.desc()).offset(skip).limit(limit).all()

    for order in orders:
        if isinstance(order.items, str):
            try:
                order.items = json.loads(order.items)
            except json.JSONDecodeError:
                order.items = []

    return orders


def get_order(db: Session, order_id: str):
    order = db.query(OrderDB).filter(OrderDB.id == order_id).first()
    if order and isinstance(order.items, str):
        try:
            order.items = json.loads(order.items)
        except json.JSONDecodeError:
            order.items = []
    return order


def fix_existing_orders(db: Session):
    """Fix existing orders with stringified JSON in items"""
    orders = db.query(OrderDB).all()
    fixed_count = 0
    for order in orders:
        if isinstance(order.items, str):
            try:
                order.items = json.loads(order.items)
                fixed_count += 1
            except json.JSONDecodeError:
                order.items = []
    db.commit()
    return fixed_count