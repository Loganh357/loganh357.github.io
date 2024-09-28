import sqlite3
import cgi

# Connect to the database
conn = sqlite3.connect('signup.db')
c = conn.cursor()

# Get form data
form = cgi.FieldStorage()
search_name = form.getvalue('search_name')

# Search for the user
c.execute("SELECT first_name, last_initial, dob, email, derp_coins, role FROM users WHERE first_name=?", (search_name,))
rows = c.fetchall()

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Search Results</title>")
print("</head>")
print("<body>")
print("<h2>Search Results</h2>")
if rows:
    for row in rows:
        print(f"<p>First Name: {row[0]}, Last Name Initial: {row[1]}, Date of Birth: {row[2]}, Email: {row[3]}, Derp Coins: {row[4]}, Role: {row[5]}</p>")
else:
    print("<p>No user found</p>")
print("</body>")
print("</html>")

# Close the connection
conn.close()
