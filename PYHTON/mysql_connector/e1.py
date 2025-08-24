import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="3936",
    database="giraffe"
)
cursor = conn.cursor()
print("Connected!")

cursor.execute("""
CREATE TABLE IF NOT EXISTS animals (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    species VARCHAR(255)
)
""")
# Single insert
cursor.execute("INSERT INTO animals (name, species) VALUES (%s, %s)", ("Leo", "Lion"))
conn.commit()

# Multiple insert
data = [("Ellie", "Elephant"), ("Zara", "Zebra")]
cursor.executemany("INSERT INTO animals (name, species) VALUES (%s, %s)", data)
conn.commit()


cursor.execute("SELECT * FROM animals")
rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.execute("UPDATE animals SET species = %s WHERE name = %s", ("African Lion", "Leo"))


