from pydantic import BaseModel, Field


class Product(BaseModel):
    id: int
    name: str = Field(min_length=3, max_length=80)
    price: float = Field(gt=0)
    stock: int = Field(ge=0)
    
class ProductCreate(BaseModel):
    name: str = Field(min_length=3, max_length=80)
    price: float = Field(gt=0)
    stock: int = Field(ge=0)
    