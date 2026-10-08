from pydantic import BaseModel, Field


class ProductCreate(BaseModel):
    name: str = Field(min_length=3, max_length=80)
    price: float = Field(gt=0)
    stock: int = Field(ge=0)

class ProductUpdate(BaseModel):
    name: str = Field(default=None, min_length=3, max_length=80)
    price: float = Field(default=0, gt=0)
    stock: int = Field(default=0, ge=0)

class ProductResponse(BaseModel):
    name: str 
    price: float
    stock: int