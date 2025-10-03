# Mpepo Kitchen Smart POS API

A FastAPI backend for a Smart Point-of-Sale system with JWT authentication and Smart E-Invoicing.

## Table of Contents

* [Features](#features)
* [Tech Stack](#tech-stack)
* [Getting Started](#getting-started)
* [Environment Variables](#environment-variables)
* [Running the Application](#running-the-application)
* [API Endpoints](#api-endpoints)
* [Database](#database)
* [Seeding Data](#seeding-data)
* [Health Check](#health-check)
* [Troubleshooting](#troubleshooting)

---

## Features

* JWT authentication (login, token)
* Products CRUD API
* Orders CRUD API
* Reports API (Sales, Inventory)
* MySQL database integration
* CORS enabled
* Automatic database creation and seeding

---

## Tech Stack

* **Python 3.11+**
* **FastAPI**
* **SQLAlchemy**
* **MySQL / MariaDB**
* **Uvicorn** (ASGI server)
* **Pydantic** (data validation)

---

## Getting Started

1. **Clone the repository**

```bash
git clone https://github.com/Freza-Mwenda/mpepo_kitchen_pos_api.git
cd mpepo_kitchen_pos_api
```

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the root directory with the following variables:

```env
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=mpepo_pos
SECRET_KEY=your_jwt_secret_key
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## Running the Application

1. **Start the API**

```bash
uvicorn main:app --reload
```

2. **Access the API docs**

* Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
* ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## API Endpoints

| Path                     | Method | Description          |
| ------------------------ | ------ | -------------------- |
| `/api/auth/login`        | POST   | User login           |
| `/api/auth/register`     | POST   | User registration    |
| `/api/products`          | GET    | List all products    |
| `/api/products/{id}`     | GET    | Get product by ID    |
| `/api/orders`            | GET    | List all orders      |
| `/api/orders/{id}`       | GET    | Get order by ID      |
| `/api/reports/sales`     | GET    | Get sales report     |
| `/api/reports/inventory` | GET    | Get inventory report |
| `/health`                | GET    | Health check         |

---

## Database

* The app uses **SQLAlchemy** to connect to a MySQL database.
* Tables are automatically created on app startup.
* Modify `configs/database.py` if you want a different database engine.

---

## Seeding Data

* `configs/seed_data.py` contains logic to populate the database with initial products, users, and sample orders.
* The database is seeded automatically on application startup.

---

## Health Check

* `/health` endpoint checks database connectivity.
* Example response:

```json
{
  "status": "healthy",
  "database": "connected"
}
```

---

## Troubleshooting

* **Database connection issues:** Ensure MySQL is running and credentials in `.env` are correct.
* **Port conflicts:** Change the port in `uvicorn.run()` if 8000 is already in use.
* **CORS issues:** Update `allow_origins` in `main.py` if frontend is hosted on a different domain.

---

### Run in Production

Use a production-ready ASGI server like **Gunicorn** with **Uvicorn workers**:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
