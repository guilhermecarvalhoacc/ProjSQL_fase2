
from sqlalchemy.orm import Session

import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item




def create_cart(db: Session, cart: schemas.CartCreate):
    cart = models.Cart()
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



def create_product(db: Session, product: schemas.ProductCreate):
    product = models.Product(quantity=product.quantity)
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