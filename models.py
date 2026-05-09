from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum


class Category(str, Enum):
    electronics = "electronics"
    clothing = "clothing"
    food = "food"
    books = "books"
    other = "other"


class ProductBase(BaseModel):
    name: str = Field(min_length=1, max_length=100, examples=["Laptop"])
    description: Optional[str] = Field(default=None, max_length=500)
    price: float = Field(gt=0, examples=[999.99])
    stock: int = Field(ge=0, examples=[10])
    category: Category = Field(default=Category.other)


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int

    model_config = {"from_attributes": True}


class OrderStatus(str, Enum):
    pending = "pending"
    confirmed = "confirmed"
    shipped = "shipped"
    delivered = "delivered"
    cancelled = "cancelled"


class OrderItemBase(BaseModel):
    product_id: int = Field(gt=0, examples=[1])
    quantity: int = Field(gt=0, examples=[2])


class OrderBase(BaseModel):
    customer_name: str = Field(min_length=1, max_length=100, examples=["John Doe"])
    customer_email: str = Field(examples=["john@example.com"])
    items: list[OrderItemBase] = Field(min_length=1)


class OrderCreate(OrderBase):
    pass


class OrderItem(OrderItemBase):
    unit_price: float
    subtotal: float


class Order(BaseModel):
    id: int
    customer_name: str
    customer_email: str
    items: list[OrderItem]
    total: float
    status: OrderStatus