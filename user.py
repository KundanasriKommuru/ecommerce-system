from db import cursor, conn
def register():
    name = input("Enter name:")
    password = input("Enter password:")
    cursor.execute("INSERT INTO users(name,password) VALUES (%s,%s)",(name,password))
    conn.commit()
    print("User resgistered!")

def login():
    name = input("Enter name:")
    password = input("Enter password:")
    cursor.execute("SELECT*FROM users WHERE name=%s AND password=%s",(name,password))
    user = cursor.fetchone()

    if user:
        print("Login successful!")
        return user[0]
    else:
        print("Invalid login")
        return None