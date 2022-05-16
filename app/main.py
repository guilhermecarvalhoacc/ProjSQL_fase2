from typing import List
from urllib import response

import uvicorn
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException, status, Path

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
@app.get("/", tags=['Root'])
def root():
    return {"Message": "Welcome to The Shop Cart"}


# Cart -------------------------------------------------------------------
# criar carrinho de compras - OK 
@app.post("/cart/", response_model=schemas.Cart, status_code=status.HTTP_201_CREATED, tags=["Cart"]) 
def create_cart(cart: schemas.CartCreate, db: Session = Depends(get_db)):
    return crud.create_cart(db=db, cart=cart)

# ADICIONAL - ler carrinho de compras - OK
@app.get("/cart/{cart_id}", tags=["Cart"])
async def read_cart(id_cart: int, db: Session = Depends(get_db)):
    db_cart = crud.get_cart(db, id_cart=id_cart)
    if not db_cart:
        raise HTTPException(status_code=404, detail="Cart not found")
    return db_cart
    

# ADICIONAL - ler carrinhos de compras existentes - OK
@app.get("/carts/", tags=["Cart"])
async def read_carts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    carts = crud.get_carts(db, skip=skip, limit=limit)
    if not carts:
        raise HTTPException(status_code=404, detail="No carts yet")
    return carts

# deletar carrinho de compras - OK
@app.delete("/cart/{id_cart}", tags=['Cart'])
def delete_cart(id_cart: int = Path(..., title="The ID of the cart to get", ge=0), db: Session = Depends(get_db)):
    cart = crud.del_cart(db, id_cart=id_cart)
    if not cart:
        return HTTPException(status_code=404, detail="Cart not found")
    return {"message": "Cart removed"}

# Product -------------------------------------------------------------------
# criar carrinho de compras - OK 
@app.post("/inventory/", response_model=schemas.Product, status_code=status.HTTP_201_CREATED, tags=['Inventory']) 
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db=db, product=product)

# consultar produto em inventario de produtos - OK
@app.get("/inventory/{id_product}", response_model=schemas.Product, tags=['Inventory']) 
def read_product(id_product: int, db: Session = Depends(get_db)):
    db_product = crud.get_product(db, id_product = id_product)
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

# consultar inventario de produtos - OK
@app.get("/inventory/", tags=['Inventory'])
def read_all_inventory(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    all_products = crud.get_products(db, skip=skip, limit=limit)
    if not all_products:
        return HTTPException(status_code=404, detail="No products yet")
    return all_products

# remover produto do inventario - OK
@app.delete("/inventory/{id_product}", tags=['Inventory'])
def delete_product(id_product: int, db: Session = Depends(get_db)):
    product = crud.del_product(db, id_product=id_product)
    if not product:
        return HTTPException(status_code=404, detail="Product not found")
    return {"message": "Cart removed"}

# alterar produto do inventario
# envia o que quer alterar pelo request body
@app.patch("/inventory/{product_id}")
def update_product(product_id: int, product: schemas.ProductBase, db: Session = Depends(get_db)):
    #product = crud.update_product()
    return 



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






# exemplos --------------------------------------------------
# @app.get("/users/", response_model=List[schemas.User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = crud.get_users(db, skip=skip, limit=limit)
#     return users




# @app.post("/users/{user_id}/items/", response_model=schemas.Item)
# def create_item_for_user(
#     user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
# ):
#     return crud.create_user_item(db=db, item=item, user_id=user_id)

