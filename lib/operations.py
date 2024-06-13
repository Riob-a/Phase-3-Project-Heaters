from models import Customer, MenuItem, Order, OrderItem, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

def add_customer(name, email):
    new_customer = Customer(name=name, email=email)
    session.add(new_customer)
    session.commit()

def add_menu_item(name, price):
    new_item = MenuItem(name=name, price=price)
    session.add(new_item)
    session.commit()

def place_order(customer_id, items):
    new_order = Order(customer_id=customer_id)
    session.add(new_order)
    session.commit()
    
    for item_id, quantity in items.items():
        order_item = OrderItem(order_id=new_order.order_id, item_id=item_id, quantity=quantity)
        session.add(order_item)
    session.commit()

def get_all_customers():
    return session.query(Customer).all()

def get_all_menu_items():
    return session.query(MenuItem).all()

def get_all_orders():
    return session.query(Order).all()

def get_order_details(order_id):
    order = session.query(Order).filter_by(order_id=order_id).first()
    if order:
        return {
            'order_id': order.order_id,
            'customer_name': order.customer.name,
            'order_date': order.order_date,
            'items': [{'name': item.menu_item.name, 'quantity': item.quantity} for item in order.order_items]
        }
    return None

def delete_customer(customer_id):
    customer = session.query(Customer).filter_by(customer_id=customer_id).first()
    if customer:
        session.delete(customer)
        session.commit()
        return True
    return False

def delete_menu_item(item_id):
    item = session.query(MenuItem).filter_by(item_id=item_id).first()
    if item:
        session.delete(item)
        session.commit()
        return True
    return False

def delete_order(order_id):
    order = session.query(Order).filter_by(order_id=order_id).first()
    if order:
        session.delete(order)
        session.commit()
        return True
    return False