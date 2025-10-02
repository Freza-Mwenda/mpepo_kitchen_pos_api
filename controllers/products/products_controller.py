from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from configs.database import get_db
from dtos.product_dtos import Product, ProductCreate
from services.products.products_service import get_products, get_product, create_product, update_product, delete_product

router = APIRouter()

# Product endpoints
@router.get("", response_model = List[Product])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = get_products(db, skip=skip, limit=limit)
    return products


@router.get("/{product_id}", response_model=Product)
def read_product(product_id: str, db: Session = Depends(get_db)):
    db_product = get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


@router.post("", response_model=Product)
def create_new_product(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db, product.dict())


@router.put("/{product_id}", response_model=Product)
def update_existing_product(product_id: str, product: ProductCreate, db: Session = Depends(get_db)):
    db_product = update_product(db, product_id, product.dict())
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


@router.delete("/{product_id}")
def delete_existing_product(product_id: str, db: Session = Depends(get_db)):
    success = delete_product(db, product_id)
    if not success:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}