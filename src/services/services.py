from src.schemas.schemas import ProductCreate, ProductUpdate

product_db = [{"id": 1, "name": "p1", "price": 1.2, "stock": 1}, {"id": 2, "name": "prod2", "price": 100, "stock": 20}]


def post_product(product: ProductCreate):
    new_id = max([p["id"] for p in product_db], default=0) + 1
    
    new_product = product.model_dump()
    new_product["id"] = new_id
    
    product_db.append(new_product)
    return new_product

def get_all_products():
    return product_db

def get_product_id(id: int):
    for p in product_db:
        if p["id"] == id:
            return p
        
def update_product(id: int, product: ProductUpdate):
    update_product = None
    for p in product_db:
        if p["id"] == id:
            update_product = p
            break
        
    data = product.model_dump(exclude_unset=True)
    update_product.update(data)
    return update_product