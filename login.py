import cgi

# Get form data
form = cgi.FieldStorage()
email = form.getvalue('email')

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Login</title>")
print("</head>")
print("<body>")

if email == "hamptonlogan562@gmail.com":
    print("<h2>Owner Page</h2>")
    print('<form action="search.py" method="get">')
    print('<label for="search_name">Search by First Name:</label><br>')
    print('<input type="text" id="search_name" name="search_name"><br><br>')
    print('<input type="submit" value="Search">')
    print('</form>')
    print('<form action="view.py" method="get">')
    print('<input type="submit" value="View All Users">')
    print('</form>')
else:
    print("<h2>Access Denied</h2>")
    print("<p>You do not have permission to view this page.</p>")

print("</body>")
print("</html>")
