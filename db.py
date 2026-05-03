import mysql.connector
conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Kundana@1208",
    database = "ecommerce_db"
)

cursor = conn.cursor()