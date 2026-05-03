from db import cursor,conn
def place_order(user_id):
    product_id = int(input("Enter product ID:"))
    
    query = f"INSERT INTO orders (user_id, product_id) VALUES ({user_id}, {product_id})"
    cursor.execute(query)
    conn.commit()
    
    print("Order placed!")

def view_orders(user_id):
    cursor.execute(f"SELECT * FROM orders WHERE user_id={user_id}")
    for row in cursor.fetchall():
        print("order ID:", row[0])
        print("user ID:", row[1])
        print("Product ID:", row[2])
        print("-------------------")

def show_summary():
    cursor.execute("SELECT COUNT(*) FROM users")
    users = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM products")
    products = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM orders")
    orders = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(DISTINCT user_id) FROM orders")
    active_users = cursor.fetchone()[0]

    print("\n--- SUMMARY ---")
    print("Total Users:", users)
    print("Total Products:", products)
    print("Total Orders:", orders)
    print("Users who placed orders:", active_users)
    print("----------------")
