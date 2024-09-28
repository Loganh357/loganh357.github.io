import sqlite3
import cgi

# Connect to the database
conn = sqlite3.connect('signup.db')
c = conn.cursor()

# Get form data
form = cgi.FieldStorage()
email = form.getvalue('email')

# Update role to Godly Derp
c.execute("UPDATE users SET role='Godly Derp' WHERE email=?", (email,))

# Commit and close the connection
conn.commit()
conn.close()

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Role Updated</title>")
print("</head>")
print("<body>")
print("<h2>Role Updated to Godly Derp</h2>")
print("</body>")
print("</html>")
