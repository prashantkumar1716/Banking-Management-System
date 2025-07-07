import mysql.connector as myconn

def connect():
    return myconn.connect(
        host="localhost",
        user="root",
        password="Bhai@12345",
        database="bank_system"
    )