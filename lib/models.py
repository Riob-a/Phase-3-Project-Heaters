from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
import datetime

Base = declarative_base()

class Customer(Base):
    __tablename__ = "customers"
    customer_id = Column(Integer, primary_key=True)
    name = Column(String, nullable= False)
    email = Column(String, nullable= False, unique=True)

class MenuItem(Base):
    __tablename__ = "menu_items"
    item_id = Column(Integer, primary_key= True)
    name = Column(String, nullable= False)
    price = Column(Float, nullable= False)

class Order(Base):
    __tablename__ = "orders"
    order_id = Column(Integer, primary_key= True)
    customer_id = Column(Integer, ForeignKey('customers.customer_id'), nullable= False)
    order_date = Column(DateTime, default=datetime.datetime.utcnow)
    
    customer = relationship("Customer", back_populates="orders")
    order_items = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")


Customer.orders = relationship("Order", order_by= Order.order_id, back_populates="customer")

class OrderItem(Base):
    __tablename__ = "order_items"
    order_item_id = Column(Integer, primary_key= True)
    order_id = Column(Integer, ForeignKey("orders.order_id"), nullable= False)
    item_id = Column(Integer, ForeignKey("menu_items.item_id"), nullable= False)
    quantity = Column(Integer, nullable= False)

    order = relationship("Order", back_populates="order_items")
    menu_item = relationship("MenuItem")

engine = create_engine('sqlite:///restaurant.db')
Base.metadata.create_all(engine)
