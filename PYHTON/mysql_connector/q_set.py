import mysql.connector as sqLtor


mycon=sqLtor.connect(
    host="Localhost",
    user="root",
    password="3936",
    
)
    
if mycon.is_connected:
    print("connnected")

my_curr= mycon.cursor()

my_curr.execute("USE school")
my_curr.execute("""CREATE TABLE student (
    roll INT PRIMARY KEY,
    name VARCHAR(50),
    marks INT
)""")

my_curr.execute("SHOW TABLES")
for i in my_curr:
    print(i)
