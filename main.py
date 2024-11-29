from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

# Define the Product model
class Product(BaseModel):
    name: str
    description: str
    price: float

# Initialize FastAPI app
app = FastAPI()

# In-memory storage for products
products_db = []

# Root route
@app.get("/")
def read_root():
    return {"message": "Welcome to the Product API!"}

# POST /products - Create a new product
@app.post("/products", status_code=201)
def create_product(product: Product):
    # Validate input fields
    if not product.name or not product.description or product.price <= 0:
        raise HTTPException(status_code=400, detail="Invalid product data")
    
    # Save the product to the in-memory database
    products_db.append(product)
    return product

# GET /products - Retrieve all products
@app.get("/products", response_model=List[Product])
def get_products():
    return products_db
