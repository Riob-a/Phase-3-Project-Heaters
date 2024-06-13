from operations import (
    add_customer, add_menu_item, place_order, get_all_customers, get_all_menu_items, get_all_orders, 
    get_order_details, delete_customer, delete_menu_item, delete_order
    )

def main():
    while True:
        print("\n---Heaters Restaurant Management System---")
        print("1. Add Customer")
        print("2. Add Menu Item")
        print("3. Place Order")
        print("4. View All Customers")
        print("5. View All Menu Items")
        print("6. View All Orders")
        print("7. View Order Details")
        print("8. Delete Customer")
        print("9. Delete Menu Item")
        print("10. Delete Order")
        print("11. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter customer name: ")
            email = input("Enter customer email: ")
            add_customer(name, email)
            print("Customer added successfully!")

        elif choice == "2":
            name = input("Enter menu item name: ")
            price = float(input("Enter menu item price: "))
            add_menu_item(name, price)
            print("Menu item added successfully!")
        
        elif choice == "3":
            customer_id = int(input("Enter customer ID: "))
            items = {}
            while True:
                item_id = int(input("Enter menu item ID (0 to stop): "))
                if item_id == 0:
                    break
                quantity = int(input("Enter quantity: "))
                items[item_id] = quantity
            place_order(customer_id, items)
            print("Order placed successfully.")

        elif choice == "4":
            customers = get_all_customers()
            for customer in customers:
                print(f"ID: {customer.customer_id}, Name: {customer.name}, Email: {customer.email}")

        elif choice == "5":
            menu_items = get_all_menu_items()
            for item in menu_items:
                print(f"ID: {item.item_id}, Name: {item.name}, Price: {item.price}")

        elif choice == "6":
            orders = get_all_orders()
            for order in orders:
                print(f"Order ID: {order.order_id}, Customer ID: {order.customer_id}, Order Date: {order.order_date}")

        elif choice == "7":
            order_id = int(input("Enter order ID: "))
            details = get_order_details(order_id)
            if details:
                print(f"Order ID: {details['order_id']}")
                print(f"Customer Name: {details['customer_name']}")
                print(f"Order Date: {details['order_date']}")
                print("Items:")
                for item in details ["items"]:
                    print(f"  - {item['name']}: {item['quantity']}")
            else:
                print("Order not Found 🤔")

        elif choice == '8':
            customer_id = int(input("Enter customer ID to delete: "))
            if delete_customer(customer_id):
                print("Customer unfortunately deleted successfully.")
            else:
                print("Customer not found 😬.")
        
        elif choice == '9':
            item_id = int(input("Enter menu item ID to delete: "))
            if delete_menu_item(item_id):
                print("Menu item deleted successfully.")
            else:
                print("Menu item not found 😬.")
        
        elif choice == '10':
            order_id = int(input("Enter order ID to delete: "))
            if delete_order(order_id):
                print("Order deleted successfully.")
            else:
                print("Order not found 😬.")

        elif choice == '11':
            break
        
        else:
            print("Invalid choice. Please try again .")

if __name__ == '__main__':
    main()

