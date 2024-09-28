import sqlite3
import cgi

# Connect to the database
conn = sqlite3.connect('signup.db')
c = conn.cursor()

# Create table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS users
             (first_name text, last_initial text, dob text, email text)''')

# Get form data
form = cgi.FieldStorage()
first_name = form.getvalue('first_name')
last_initial = form.getvalue('last_initial')
dob = form.getvalue('dob')
email = form.getvalue('email')

# Insert data into the table
c.execute("INSERT INTO users (first_name, last_initial, dob, email) VALUES (?, ?, ?, ?)",
          (first_name, last_initial, dob, email))

# Commit and close the connection
conn.commit()
conn.close()

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Signup Successful</title>")
print("</head>")
print("<body>")
print("<h2>Signup Successful</h2>")
print("</body>")
print("</html>")
