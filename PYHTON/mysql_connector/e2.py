import mysql.connector as sqLtor


mycon=sqLtor.connect(
    host="Localhost",
    user="root",
    password="3936",
    
)
    
if mycon.is_connected:
    print("connected sucessfully")