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
    # Sample products data with Decimal prices and image URLs
    sample_products = [
        {
            "id": "1",
            "name": "Grilled Chicken",
            "price": Decimal("18.99"),
            "category": "Main Course",
            "description": "Juicy grilled chicken with herbs and spices",
            "image_url": "https://example.com/images/grilled_chicken.jpg"
        },
        {
            "id": "2",
            "name": "Beef Burger",
            "price": Decimal("15.99"),
            "category": "Main Course",
            "description": "Classic beef burger with cheese and vegetables",
            "image_url": "https://example.com/images/beef_burger.jpg"
        },
        {
            "id": "3",
            "name": "French Fries",
            "price": Decimal("5.99"),
            "category": "Side Dish",
            "description": "Crispy golden fries with seasoning",
            "image_url": "https://example.com/images/french_fries.jpg"
        },
        {
            "id": "4",
            "name": "Greek Salad",
            "price": Decimal("12.99"),
            "category": "Salad",
            "description": "Fresh vegetables with feta cheese and olive oil",
            "image_url": "https://example.com/images/greek_salad.jpg"
        },
        {
            "id": "5",
            "name": "Coca Cola",
            "price": Decimal("3.99"),
            "category": "Beverage",
            "description": "Cold refreshing carbonated drink",
            "image_url": "https://example.com/images/coca_cola.jpg"
        },
        {
            "id": "6",
            "name": "Ice Cream",
            "price": Decimal("6.99"),
            "category": "Dessert",
            "description": "Vanilla ice cream with chocolate sauce",
            "image_url": "https://example.com/images/ice_cream.jpg"
        },
        {
            "id": "7",
            "name": "Chicken Wings",
            "price": Decimal("11.99"),
            "category": "Appetizer",
            "description": "Spicy chicken wings with dip sauce",
            "image_url": "https://example.com/images/chicken_wings.jpg"
        },
        {
            "id": "8",
            "name": "Pasta Carbonara",
            "price": Decimal("14.99"),
            "category": "Main Course",
            "description": "Creamy pasta with bacon and parmesan",
            "image_url": "https://example.com/images/pasta_carbonara.jpg"
        },
        {
            "id": "9",
            "name": "Chocolate Cake",
            "price": Decimal("7.99"),
            "category": "Dessert",
            "description": "Rich chocolate cake with ganache",
            "image_url": "https://example.com/images/chocolate_cake.jpg"
        },
        {
            "id": "10",
            "name": "Lemonade",
            "price": Decimal("4.50"),
            "category": "Beverage",
            "description": "Freshly squeezed lemonade with mint",
            "image_url": "https://example.com/images/lemonade.jpg"
        }
    ]
    
    # Add products to database
    for product_data in sample_products:
        product = ProductDB(**product_data)
        db.add(product)
    
    db.commit()
    db.close()
    print("✅ Database seeded with sample data!")