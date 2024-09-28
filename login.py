import sqlite3
import cgi

# Connect to the database
conn = sqlite3.connect('signup.db')
c = conn.cursor()

# Get form data
form = cgi.FieldStorage()
email = form.getvalue('email')

# Check if the user exists
c.execute("SELECT first_name, role FROM users WHERE email=?", (email,))
row = c.fetchone()

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Login</title>")
print("</head>")
print("<body>")

if row:
    first_name, role = row
    print(f"<h2>Welcome, {first_name} ({role})</h2>")
    print('<a href="chat.html">Go to Chat</a>')
else:
    print("<h2>Login Failed</h2>")
    print("<p>User not found.</p>")

print("</body>")
print("</html>")

# Close the connection
conn.close()
