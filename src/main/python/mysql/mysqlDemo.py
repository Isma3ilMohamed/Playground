import mysql.connector

# establish the connection

conn = mysql.connector.connect(
    host='localhost',
    user='yourusername',
    password='yourpassword',
    database='yourdatabase'
)

# Create a cursor object
cursor = conn.cursor()
# Execute a query
cursor.execute("SELECT * FROM yourtable")

# Fetch and print the results
results = cursor.fetchall()
for row in results:
    print(row)

# Close the connection
conn.close()

# Creating a Table

cursor.execute("""
    CREATE TABLE employees (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        position VARCHAR(255)
    )
""")

# Inserting Data
cursor.execute("""
    INSERT INTO employees (name, position)
    VALUES (%s, %s)
""", ('John Doe', 'Software Engineer'))
conn.commit()

# Querying Data
cursor.execute("SELECT * FROM employees WHERE position = 'Software Engineer'")
results = cursor.fetchall()
for row in results:
    print(row)
