from typing import List

import uvicorn
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException, status

import models, schemas, crud
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# root - OK
@app.get("/")
async def root():
    return {"Message": "Welcome to The Shop Cart"}


# Cart -------------------------------------------------------------------
# criar carrinho de compras - OK 
@app.post("/cart/", response_model=schemas.Cart, status_code=status.HTTP_201_CREATED) 
async def create_cart(cart: schemas.CartCreate, db: Session = Depends(get_db)):
    return crud.create_cart(db=db, cart=cart)

# @app.post("/users/", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = crud.get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.create_user(db=db, user=user)

# # deletar carrinho de compras - OK
# @app.delete("/cart/{cart_id}", response_model=Cart)
# async def delete_cart(*, cart_id: int = Path(..., title="The ID of the cart to get", ge=0)):
#     remove_from_json(cart_id,"carts.json", "carts", "cart", 0)
#     return 

# # ADICIONAL - ler carrinho de compras - OK
# @app.get("/cart/{cart_id}")
# async def read_cart(*, cart_id: int):
#     carts = read_json("carts.json", "carts")

#     for cart in carts:
#         if cart["cart_id"] == cart_id:
#             return cart
    
#     return {"message": "Not Found"}
    

# # ADICIONAL - ler carrinhos de compras existentes - OK
# @app.get("/carts/")
# async def read_carts():
#     carts = read_json("carts.json", "carts")
#     if len(carts) == 0:
#         return {"message": "No Carts Yet"}
#     return {"Carts Avaiable": carts}

# # adicionar item ao carrinho de compras
# # envia dados pelo request body
# @app.patch("/cart/{cart_id}/product")
# async def add_to_cart(cart_id:int, product: Product):
    
#     update_json(cart_id, product,"carts.json","carts", 1, product.product_id)
#     return 

# # remover item carrinho de compras 
# # como defino a quantidade de itens que vou remover?
# @app.delete("/cart/{cart_id}/product/{product_id}")
# async def remove_from_cart(cart_id:int, product_id: int):
#     remove_from_json(cart_id,"carts.json", "carts", "product",  1, product_id )
#     return 

# # criar produto
# # envia dados pelo request body - OK
# @app.post("/inventory/", status_code=status.HTTP_201_CREATED)
# async def create_product(product: Product_without_id):
#     append_json(product, "inventory.json", "inventory", "product")
#     return product

# # consultar inventario de produtos - OK
# @app.get("/inventory/")
# async def read_all_inventory():
#     all_products = read_json("inventory.json", "inventory")

#     return all_products

# # consultar produto em inventario de produtos - OK
# @app.get("/inventory/{product_id}") 
# async def read_product(*, product_id: int):
#     all_products = read_json("inventory.json", "inventory")
#     for p in all_products:
#         if p["product_id"] == product_id:
#             return p
    
#     return {"message": "Not Found"}

# # alterar produto do inventario
# # envia o que quer alterar pelo request body
# @app.patch("/inventory/{product_id}")
# async def update_product(product_id: int, product: Product):
#     update_json(product_id, product,"inventory.json","inventory", 0)
#     return 

# # remover produto do inventario - OK
# @app.delete("/inventory/{product_id}")
# async def delete_product(product_id: int):
#     remove_from_json(product_id, "inventory.json", "inventory", "product", 0)
#     return 

# exemplos --------------------------------------------------
# @app.get("/users/", response_model=List[schemas.User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = crud.get_users(db, skip=skip, limit=limit)
#     return users


# @app.get("/users/{user_id}", response_model=schemas.User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = crud.get_user(db, user_id=user_id)
#     if not db_user:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user


# @app.post("/users/{user_id}/items/", response_model=schemas.Item)
# def create_item_for_user(
#     user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
# ):
#     return crud.create_user_item(db=db, item=item, user_id=user_id)


# @app.get("/items/", response_model=List[schemas.Item])
# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     items = crud.get_items(db, skip=skip, limit=limit)
#     return items