import sqlite3

def update_role(email, derp_coins):
    role = 'New Derp'
    if derp_coins >= 1000000000:
        role = 'Master Derp'
    elif derp_coins >= 10000000:
        role = 'Rare Derp'
    elif derp_coins >= 20000:
        role = 'Classic Derp'
    elif email == 'hamptonlogan562@gmail.com':
        role = 'Godly Derp'

    return role

# Connect to the database
conn = sqlite3.connect('signup.db')
c = conn.cursor()

# Retrieve all users
c.execute("SELECT email, derp_coins FROM users")
rows = c.fetchall()

# Update roles
for row in rows:
    email, derp_coins = row
    role = update_role(email, derp_coins)
    c.execute("UPDATE users SET role=? WHERE email=?", (role, email))

# Commit and close the connection
conn.commit()
conn.close()
