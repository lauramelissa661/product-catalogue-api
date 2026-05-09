# Simple in-memory "database" using dicts
# In production this would be replaced with a real DB (e.g. PostgreSQL)

from app.models import Product, Order

products_db: dict[int, Product] = {
    1: Product(id=1, name="Laptop", description="14-inch laptop, 16GB RAM", price=999.99, stock=10, category="electronics"),
    2: Product(id=2, name="Python Book", description="Learn Python the hard way", price=29.99, stock=50, category="books"),
    3: Product(id=3, name="T-Shirt", description="100% cotton, size M", price=14.99, stock=100, category="clothing"),
}

orders_db: dict[int, Order] = {}

product_id_counter: int = 4
order_id_counter: int = 1


def next_product_id() -> int:
    global product_id_counter
    pid = product_id_counter
    product_id_counter += 1
    return pid


def next_order_id() -> int:
    global order_id_counter
    oid = order_id_counter
    order_id_counter += 1
    return oid