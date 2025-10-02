from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import text
from configs.database import get_db, create_tables
from controllers.authentication import auth_controller
from controllers.orders import orders_controller
from controllers.products import products_controller
from controllers.reports import reports_controller
from configs.seed_data import seed_database

# Create FastAPI app
app = FastAPI(
    title="Mpepo Kitchen Smart POS API",
    version="1.0.0",
    description="Smart Point-of-Sale system with JWT authentication and Smart E-Invoicing"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth_controller.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(products_controller.router, prefix="/api/products", tags=["Products"])
app.include_router(orders_controller.router, prefix="/api/orders", tags=["Orders"])
app.include_router(reports_controller.router, prefix="/api/reports", tags=["Reports"])


# Create tables and seed data on startup
@app.on_event("startup")
def on_startup():
    try:
        create_tables()
        seed_database()
        print("✅ Database initialized successfully!")
    except Exception as e:
        print(f"❌ Database initialization failed: {e}")


# Health check endpoint
@app.get("/")
async def root():
    return {"message": "Mpepo Kitchen POS API with MySQL is running"}


@app.get("/health")
async def health_check(db: Session = Depends(get_db)):
    """Database health check"""
    try:
        db.execute(text("SELECT 1"))
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        return {"status": "unhealthy", "database": "disconnected", "error": str(e)}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)