# Product Catalogue API

A REST API for managing products and orders. Built with FastAPI and hosted on AWS S3.

## What it does

- Browse, create, update and delete products
- Place orders with automatic stock validation
- Auto-generated API docs at `/docs`

## Tech Stack

- Python 3.12 + FastAPI
- Pydantic v2
- pytest (18 tests)
- AWS S3

## How to run

```bash
# Install dependencies
pip install -r requirements.txt

# Run the API
uvicorn app.main:app --reload
```

API runs at `http://localhost:8000`  
Swagger docs at `http://localhost:8000/docs`

## Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/products/` | List all products |
| POST | `/products/` | Create a product |
| PUT | `/products/{id}` | Update a product |
| DELETE | `/products/{id}` | Delete a product |
| GET | `/orders/` | List all orders |
| POST | `/orders/` | Place an order |
| PATCH | `/orders/{id}/status` | Update order status |

## Run tests

```bash
python -m pytest tests/test_api.py -v
```

## Live site

http://product-catalogue-api-lauramelissa.s3-website.eu-north-1.amazonaws.com/#

---

**Laura Melissa** — Cloud Technology
