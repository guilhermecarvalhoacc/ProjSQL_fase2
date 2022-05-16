
from sqlalchemy.orm import Session

import models, schemas


# !!! PRECISA FAZER !!!
# CART ------------------------------------
# create cart - FEITO E FUNCIONANDO
# delete cart - FEITO E FUNCIONANDO
# read cart - FEITO E FUNCIONANDO
# read carts - FEITO E FUNCIONANDO
# add to cart - 
# remove from cart - 

# INVENTORY --------------------------------
# create product - FEITO E FUNCIONANDO
# read product - FEITO E FUNCIONANDO
# update product 
# delete product - FEITO E FUNCIONANDO
# read inventory - FEITO E FUNCIONANDO


# Cart -----------------------------------------------------------

# ok
def create_cart(db: Session, cart: schemas.CartCreate):
    db_cart = models.Cart(**cart.dict())
    db.add(db_cart)
    db.commit()
    db.refresh(db_cart)
    return db_cart

# ok
def get_cart(db: Session, id_cart: int):
    return db.query(models.Cart).filter(models.Cart.id_cart == id_cart).first()

# ok
def get_carts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Cart).offset(skip).limit(limit).all()

# ok
def del_cart(db: Session, id_cart:int):
    db_cart = get_cart(db, id_cart)
    if db_cart:
        db.delete(db_cart)
        db.commit()
        return db_cart
    return

def add_to_cart(db: Session, cartproduct: schemas.CartProductCreate):
    db_cartproduct = models.CartProduct(id_cart=cartproduct.id_cart,id_product=cartproduct.id_product,quantity=cartproduct.quantity)
    db.add(db_cartproduct)
    db.commit()
    db.refresh(db_cartproduct)
    return db_cartproduct


def remove_from_cart(db: Session, id_cartproduct:int):
    db.delete(db.cartproduct).where(db.cartproduct.id_cartproduct == id_cartproduct) #https://docs.sqlalchemy.org/en/14/core/dml.html
    db.commit()
    return None

# Product -----------------------------------------------------------

# ok
def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# ok
def get_product(db: Session, id_product: int):
    return db.query(models.Product).filter(models.Product.id_product == id_product).first()

# ok
def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()

# ok
def del_product(db: Session, id_product:int):
    db_product = get_product(db, id_product)
    if db_product:
        db.delete(db_product)
        db.commit()
        return db_product
    return

    
def update_product(db: Session, id_product:int, newqtd: int):
    db.update(db.product).where(db.product.id_product == id_product).values(quantity = newqtd) #https://docs.sqlalchemy.org/en/14/core/dml.html
    db.commit()
    return None


