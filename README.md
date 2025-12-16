# Product API

A simple backend API built with **FastAPI**, inspired by MercadoLibre’s product detail page.  
This project provides CRUD operations for products stored in a local JSON file.  
It is designed with **clean code principles**, modular architecture, and can be executed either with **Python** or **Docker**.

## Tech stack
- Python 3.10+
- FastAPI
- Pydantic
- Uvicorn (ASGI server)
- Pytest for tests

## 🚀 Endpoints

| Method | Endpoint               | Description                     |
|--------|------------------------|---------------------------------|
| GET    | `/products`            | Get all products                |
| GET    | `/products/{product_id}` | Get single product by ID, returns 404 if not found |
| POST   | `/products`            | Create a new product            |
| PUT    | `/products/{product_id}` | Update an existing product by ID, returns 404 if not found |
| DELETE | `/products/{product_id}` | Delete a product by ID, returns 404 if not found |
| GET    | `/health`              | Health check                    |


## How to run
See `run.md` for step-by-step instructions.

## Why FastAPI?
- Automatic interactive docs (OpenAPI / Swagger).
- Fast to develop and maintain, strong typing with Pydantic.
- Great for small API prototypes and production-ready services.

## Notes
- Data persisted locally in `app/data/products.json`.
- Tests available in `tests/test_products.py`.

## 📊 API Design
A[Frontend Client] -->|HTTP Request| B[FastAPI Backend]
