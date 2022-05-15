
from sqlalchemy.orm import Session

import models, schemas


# !!! PRECISA FAZER !!!
# CART ------------------------------------
# create cart - FEITO
# delete cart - FEITO
# read cart - FEITO
# read carts - FEITO
# add to cart
# remove from cart

# INVENTORY --------------------------------
# create product - FEITO
# read product - FEITO
# update product 
# delete product - FEITO
# read inventory - FEITO

# Cart -----------------------------------------------------------

def create_cart(db: Session, cart: schemas.CartCreate):
    db_cart = models.Cart(**cart.dict())
    db.add(db_cart)
    db.commit()
    db.refresh(db_cart)
    return db_cart

def get_cart(db: Session, id_cart: int):
    return db.query(models.cart).filter(models.cart.id_cart == id_cart).first()

def get_carts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.cart).offset(skip).limit(limit).all()

def del_cart(db: Session, id_cart:int):
    db.delete(db.cart).where(db.cart.id_cart == id_cart) #https://docs.sqlalchemy.org/en/14/core/dml.html
    db.commit()
    return None

def add_to_cart(db: Session, cartproduct: schemas.CartProductCreate):
    cart = models.CartProduct(id_cart=cartproduct.id_cart,id_product=cartproduct.id_product,quantity=cartproduct.quantity)
    db.add(db_cartproduct)
    db.commit()
    db.refresh(db_cartproduct)
    return db_cartproduct


def remove_from_cart(db: Session, id_cartproduct:int):
    db.delete(db.cartproduct).where(db.cartproduct.id_cartproduct == id_cartproduct) #https://docs.sqlalchemy.org/en/14/core/dml.html
    db.commit()
    return None

# Product -----------------------------------------------------------

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(quantity=product.quantity)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_product(db: Session, id_product: int):
    return db.query(models.product).filter(models.cart.id_product == id_product).first()

def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.product).offset(skip).limit(limit).all()

def del_product(db: Session, id_product:int):
    db.delete(db.product).where(db.product.id_product == id_product) #https://docs.sqlalchemy.org/en/14/core/dml.html
    db.commit()
    return None


def update_product(db: Session, id_product:int, newqtd: int):
    db.update(db.product).where(db.product.id_product == id_product).values(quantity = newqtd) #https://docs.sqlalchemy.org/en/14/core/dml.html
    db.commit()
    return None

# def get_user(db: Session, user_id: int):
#     return db.query(models.User).filter(models.User.id == user_id).first()


# def get_user_by_email(db: Session, email: str):
#     return db.query(models.User).filter(models.User.email == email).first()


# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.User).offset(skip).limit(limit).all()


# def create_user(db: Session, user: schemas.UserCreate):
#     fake_hashed_password = user.password + "notreallyhashed"
#     db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user


# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()


# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item