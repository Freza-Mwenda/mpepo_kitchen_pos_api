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
            "image_url": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQuBkZLiOpt0tSb3fhdk_lek5yXHWoNdKvwQDMnbtCEBNVbFIPyekMlFNeh0mdKbqWOYFQLuKBGMwLS9vmd9ceQWQUTdQT63IBha5L89w"
        },
        {
            "id": "2",
            "name": "Beef Burger",
            "price": Decimal("15.99"),
            "category": "Main Course",
            "description": "Classic beef burger with cheese and vegetables",
            "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQcoXWLIiYs_u54dOx8J_1DpCZNKBKcQJe0A&s"
        },
        {
            "id": "3",
            "name": "French Fries",
            "price": Decimal("5.99"),
            "category": "Side Dish",
            "description": "Crispy golden fries with seasoning",
            "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQcoXWLIiYs_u54dOx8J_1DpCZNKBKcQJe0A&s"
        },
        {
            "id": "4",
            "name": "Greek Salad",
            "price": Decimal("12.99"),
            "category": "Salad",
            "description": "Fresh vegetables with feta cheese and olive oil",
            "image_url": "https://i0.wp.com/www.lubzonline.com/wp-content/uploads/2021/12/131980110_691132031599382_7883691975085799914_o-1024x804-1.jpg?fit=750%2C589&ssl=1"
        },
        {
            "id": "5",
            "name": "Coca Cola",
            "price": Decimal("3.99"),
            "category": "Beverage",
            "description": "Cold refreshing carbonated drink",
            "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQcoXWLIiYs_u54dOx8J_1DpCZNKBKcQJe0A&s"
        },
        {
            "id": "6",
            "name": "Ice Cream",
            "price": Decimal("6.99"),
            "category": "Dessert",
            "description": "Vanilla ice cream with chocolate sauce",
            "image_url": "https://i0.wp.com/www.lubzonline.com/wp-content/uploads/2021/12/131980110_691132031599382_7883691975085799914_o-1024x804-1.jpg?fit=750%2C589&ssl=1"
        },
        {
            "id": "7",
            "name": "Chicken Wings",
            "price": Decimal("11.99"),
            "category": "Appetizer",
            "description": "Spicy chicken wings with dip sauce",
            "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQcoXWLIiYs_u54dOx8J_1DpCZNKBKcQJe0A&s"
        },
        {
            "id": "8",
            "name": "Pasta Carbonara",
            "price": Decimal("14.99"),
            "category": "Main Course",
            "description": "Creamy pasta with bacon and parmesan",
            "image_url": "https://i0.wp.com/www.lubzonline.com/wp-content/uploads/2021/12/131980110_691132031599382_7883691975085799914_o-1024x804-1.jpg?fit=750%2C589&ssl=1"
        },
        {
            "id": "9",
            "name": "Chocolate Cake",
            "price": Decimal("7.99"),
            "category": "Dessert",
            "description": "Rich chocolate cake with ganache",
            "image_url": "https://www.zimbokitchen.com/wp-content/uploads/2022/06/MINCE-PASTA-3-750x500.jpg"
        },
        {
            "id": "10",
            "name": "Lemonade",
            "price": Decimal("4.50"),
            "category": "Beverage",
            "description": "Freshly squeezed lemonade with mint",
            "image_url": "https://i0.wp.com/www.lubzonline.com/wp-content/uploads/2021/12/131980110_691132031599382_7883691975085799914_o-1024x804-1.jpg?fit=750%2C589&ssl=1"
        }
    ]
    
    # Add products to database
    for product_data in sample_products:
        product = ProductDB(**product_data)
        db.add(product)
    
    db.commit()
    db.close()
    print("✅ Database seeded with sample data!")