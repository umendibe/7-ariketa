from fastapi import FastAPI

from src.schemas.schemas import ProductCreate, ProductResponse, ProductUpdate
from src.services.services import (
    get_all_products,
    get_product_id,
    post_product,
    update_product,
)

app = FastAPI()

@app.get("/prodcuts", response_model=list[ProductResponse], status_code=200)
def get_products():
    return get_all_products()

@app.post("/products", status_code=201)
def create_product(product: ProductCreate):
    return post_product(product)

@app.get("/products/{id}", response_model=ProductResponse, status_code=200)
def get_by_id(id: int):
    return get_product_id(id)

@app.patch("/products/{id}", status_code=200)
def patch_product(id: int, parametro: ProductUpdate):
    return update_product(id, parametro)
