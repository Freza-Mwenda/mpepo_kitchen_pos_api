from sqlalchemy.orm import Session
import uuid
from decimal import Decimal
from models.products.product_model import ProductDB

# Product CRUD functions
def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ProductDB).filter(ProductDB.is_active == 1).offset(skip).limit(limit).all()

def get_product(db: Session, product_id: str):
    return db.query(ProductDB).filter(ProductDB.id == product_id, ProductDB.is_active == 1).first()

def create_product(db: Session, product: dict):
    db_product = ProductDB(
        id=str(uuid.uuid4()),
        name=product["name"],
        price=Decimal(str(product["price"])),
        category=product["category"],
        description=product.get("description"),
        image_url=product.get("image_url")
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product(db: Session, product_id: str, product_update: dict):
    db_product = db.query(ProductDB).filter(ProductDB.id == product_id).first()
    if db_product:
        for key, value in product_update.items():
            if key == "price":
                value = Decimal(str(value))
            setattr(db_product, key, value)
        db.commit()
        db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: str):
    db_product = db.query(ProductDB).filter(ProductDB.id == product_id).first()
    if db_product:
        db_product.is_active = 0
        db.commit()
    return db_product