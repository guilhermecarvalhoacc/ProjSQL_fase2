from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float
from database import Base
from sqlalchemy.orm import relationship


# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True, index=True)
#     email = Column(String, unique=True, index=True)
#     hashed_password = Column(String)
#     is_active = Column(Boolean, default=True)

#     items = relationship("Item", back_populates="owner")


# class Item(Base):
#     __tablename__ = "items"

#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     description = Column(String, index=True)
#     owner_id = Column(Integer, ForeignKey("users.id"))

#     owner = relationship("User", back_populates="items")

# Product ----------------------------------------------------
class Product(Base):
    __tablename__ = "Product"

    id_product = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    brand = Column(String)
    price = Column(Float)
    discount = Column(Float)
    quantity = Column(Integer)
    url_img = Column(String)

    products_inventory = relationship("CartProduct", back_populates="products_cart")

# CartProduct --------------------------------------------
class CartProduct(Base):
    __tablename__ = "CartProduct"

    id_cart = Column(Integer, ForeignKey("Cart.id_cart"), primary_key=True, index=True)
    id_product = Column(Integer, ForeignKey("Product.id_product"), primary_key=True, index=True)
    quantity = Column(Integer)

    products_cart = relationship("Product", back_populates="products_inventory")
    cart = relationship("Cart", back_populates="carts")
    
# Cart ---------------------------------------------------
class Cart(Base):
    __tablename__ = "Cart"

    id_cart = Column(Integer, ForeignKey("CartProduct.id_cart"), primary_key=True, index=True)
    id_user = Column(Integer, primary_key=True, index=True)

    carts = relationship("CartProduct", back_populates="cart")

# Product ----------------------------------------------------
class Product(Base):
    __tablename__ = "Product"

    id_product = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    brand = Column(String)
    price = Column(Float)
    discount = Column(Float)
    quantity = Column(Integer)
    url_img = Column(String)

    products_inventory = relationship("CartProduct", back_populates="products_cart")

# CartProduct --------------------------------------------
class CartProduct(Base):
    __tablename__ = "CartProduct"

    id_cart = Column(Integer, primary_key=True, index=True)
    id_product = Column(Integer, ForeignKey("Product.id_product"), primary_key=True, index=True)
    quantity = Column(Integer)

    products_cart = relationship("Product", back_populates="products_inventory")
    cart = relationship("Cart", back_populates="carts")
    
# Cart ---------------------------------------------------
class Cart(Base):
    __tablename__ = "Cart"

    id_cart = Column(Integer, ForeignKey("CartProduct.id_cart"), primary_key=True, index=True)
    id_user = Column(Integer, primary_key=True, index=True)

    carts = relationship("CartProduct", back_populates="cart")

