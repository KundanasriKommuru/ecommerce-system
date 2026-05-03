from db import cursor, conn

def add_product():
    name = input("Enter product name:")
    price = int(input("Enter price:"))

    query = f"INSERT INTO products (name, price) VALUES ('{name}', {price})"
    cursor.execute(query)
    conn.commit()

    print("Product added!")

def view_products():
    cursor.execute("SELECT * FROM products")
    for row in cursor.fetchall():
        print(row)