from typing import Optional, Dict, List, Set
from pydantic import BaseModel, Field, HttpUrl # for request body interactions



# Product ------------------------------------------------
class ProductBase(BaseModel):
    name: str = Field(None, title="The name of the product", max_length=100, example="iogurte")                              
    description: Optional[str] = Field(None, title="The description of the product", max_length=300, example="iogurte desnatado 200g")   
    brand: Optional[str] = Field(None, title="The brand of the item", max_length=80, example="nestle")   
    price: float = Field(..., gt=0, description="The price must be greater than zero", example=2.7)
    discount: Optional[float] = Field(..., ge=0, lt=1, description="The discount must be greater than 0 and less than 1", example=0.05)     
    quantity: float = Field(..., gt=0, description="The quantity must be greater than zero", example=1)
    url_img: Optional[str] = Field(..., description="The url of the product img", example="www.someproductimage.com")

class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id_product: int

    class Config:
        orm_mode = True


# Cart ---------------------------------------------------
class CartBase(BaseModel):
    id_user: int

class CartCreate(CartBase):
    pass

class Cart(CartBase):
    id_cart: int
    products: Set[str] = set() # lista de produtos unicos

    class Config:
        orm_mode = True


# # Product ------------------------------------------------
# class ProductBase(BaseModel):
#     name: str
#     description: Optional[str] = None
#     brand: str
#     price: float
#     discount: float
#     quantity: int
#     url_img:


# class ProductCreate(ProductBase):
#     pass


# class Product(ProductBase):
#     id_product: int
#     class Config:
#         orm_mode = True

# # Cart ---------------------------------------------------
# class CarttBase(BaseModel):
#     id_cart: int
#     id_user: int
#     carts: 

# class CartCreate(ProductBase):
#     pass



# class ItemBase(BaseModel):
#     title: str
#     description: Optional[str] = None


# class ItemCreate(ItemBase):
#     pass


# class Item(ItemBase):
#     id: int
#     owner_id: int

#     class Config:
#         orm_mode = True


# class UserBase(BaseModel):
#     email: str


# class UserCreate(UserBase):
#     password: str


# class User(UserBase):
#     id: int
#     is_active: bool
#     items: List[Item] = []

#     class Config:
#         orm_mode = True