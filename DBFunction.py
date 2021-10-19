#DB Name: MySQL
#DB Version: 8.0.26
#DB Port Number: 3306
#DB Download Link: 
from getpass import getpass
import mysql.connector 

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="caxzvbnM1!?",
    database="customer_accounting_db"
)

cursor = db.cursor()
cursor.execute("CREATE DATABASE customer_accounting_db")
cursor.execute("CREATE TABLE customer (id INT AUTO_INCREMENT PRIMARY KEY, NAME VARCHAR(50), totalGoods INT)")
cursor.execute("INSERT INTO customer (NAME, totalGoods) VALUES (%s,%s)", ("Albert", 13))
cursor.execute("INSERT INTO customer (NAME, totalGoods) VALUES (%s,%s)", ("James", 3))
cursor.execute("INSERT INTO customer (NAME, totalGoods) VALUES (%s,%s)", ("Kevin", 5))
cursor.execute("INSERT INTO customer (NAME, totalGoods) VALUES (%s,%s)", ("Eric", 16))
cursor.execute("INSERT INTO customer (NAME, totalGoods) VALUES (%s,%s)", ("David", 21))
db.commit()
cursor.execute("CREATE TABLE customer_order (customer_id INT, goods INT)")
cursor.execute("INSERT INTO customer_order (customer_id, goods) VALUES (%s,%s)", (6, 7))
cursor.execute("INSERT INTO customer_order (customer_id, goods) VALUES (%s,%s)", (7, 1))
cursor.execute("INSERT INTO customer_order (customer_id, goods) VALUES (%s,%s)", (8, 2))
cursor.execute("INSERT INTO customer_order (customer_id, goods) VALUES (%s,%s)", (9, 8))
cursor.execute("INSERT INTO customer_order (customer_id, goods) VALUES (%s,%s)", (10, 12))
db.commit()
cursor.execute("SELECT * FROM customer")
#cursor.execute("DESCRIBE customer")
for x in cursor:
     print(x)
cursor.execute("DELETE FROM customer WHERE NAME = 'Johny'")
db.commit()
def createCustomer(name, total_goods):
    cursor.execute("INSERT INTO customer (NAME, totalGoods) VALUES (%s,%s)", (name, total_goods))
    db.commit()
    return 0 #when the insertion is sucessful it returns 0 for testing

def createOrder(custID, goodsPurchased):
    cursor.execute("INSERT INTO customer_order (customer_id, goods) VALUES (%s,%s)", (custID, goodsPurchased))
    db.commit()

def retrieveAll():
    cursor.execute("SELECT * FROM customer")
    customerArray = []
    for x in cursor:
        customerArray.append(x)
    return customerArray