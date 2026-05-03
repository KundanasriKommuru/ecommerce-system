from src.user import register,login
from src.product import add_product,view_products
from src.order import place_order,view_orders, show_summary
while True:
    print("\n1.Register 2.Login 3.Exit")
    choice = int(input("Enter choice:"))

    if choice == 1:
        register()

    elif choice == 2:
        user_id = login()

        if user_id:
            while True:
                print("\n1.View Products 2.Add products 3.Place order 4.View orders 5.Summary 6.Logout")
                ch = int(input("enter choice:"))

                if ch == 1:
                    view_products()
                elif ch == 2:
                    add_product()
                elif ch == 3:
                    place_order(user_id)
                elif ch == 4:
                    view_orders(user_id)
                elif ch == 5:
                    show_summary()
                elif ch == 6:
                    break

    elif choice == 3:
        break