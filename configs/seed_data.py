from configs.database import SessionLocal, engine, Base
from decimal import Decimal

from models.products.product_model import ProductDB


def seed_database():
    # Create tables
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    
    # Check if products already exist
    existing_products = db.query(ProductDB).count()
    if existing_products > 0:
        db.close()
        print("Database already has data, skipping seeding.")
        return
    
    # Sample products data with Decimal prices
    sample_products = [
        {
            "id": "1", "name": "Grilled Chicken", "price": Decimal('18.99'), "category": "Main Course",
            "description": "Juicy grilled chicken with herbs and spices"
        },
        {
            "id": "2", "name": "Beef Burger", "price": Decimal('15.99'), "category": "Main Course",
            "description": "Classic beef burger with cheese and vegetables"
        },
        {
            "id": "3", "name": "French Fries", "price": Decimal('5.99'), "category": "Side Dish",
            "description": "Crispy golden fries with seasoning"
        },
        {
            "id": "4", "name": "Greek Salad", "price": Decimal('12.99'), "category": "Salad",
            "description": "Fresh vegetables with feta cheese and olive oil"
        },
        {
            "id": "5", "name": "Coca Cola", "price": Decimal('3.99'), "category": "Beverage",
            "description": "Cold refreshing carbonated drink"
        },
        {
            "id": "6", "name": "Ice Cream", "price": Decimal('6.99'), "category": "Dessert",
            "description": "Vanilla ice cream with chocolate sauce"
        },
        {
            "id": "7", "name": "Chicken Wings", "price": Decimal('11.99'), "category": "Appetizer",
            "description": "Spicy chicken wings with dip sauce"
        },
        {
            "id": "8", "name": "Pasta Carbonara", "price": Decimal('14.99'), "category": "Main Course",
            "description": "Creamy pasta with bacon and parmesan"
        }
    ]
    
    # Add products to database
    for product_data in sample_products:
        product = ProductDB(**product_data)
        db.add(product)
    
    db.commit()
    db.close()
    print("✅ Database seeded with sample data!")