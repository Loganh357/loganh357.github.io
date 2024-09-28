import sqlite3

# Connect to the database
conn = sqlite3.connect('signup.db')
c = conn.cursor()

# Retrieve all users
c.execute("SELECT * FROM users")
rows = c.fetchall()

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>All Users</title>")
print("</head>")
print("<body>")
print("<h2>All Users</h2>")
for row in rows:
    print(f"<p>First Name: {row[0]}, Last Name Initial: {row[1]}, Date of Birth: {row[2]}, Email: {row[3]}</p>")
print("</body>")
print("</html>")

# Close the connection
conn.close()
