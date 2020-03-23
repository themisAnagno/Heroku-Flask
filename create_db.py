import sqlite3

# Create the database and the users table
connection = sqlite3.connect("data.db")
cursor = connection.cursor()
create_users_table = "CREATE TABLE users (username text, password text, id text PRIMARY KEY)"
create_items_table = "CREATE TABLE items (name text, price text, id TEXT PRIMARY KEY)"
cursor.execute(create_users_table)
cursor.execute(create_items_table)
admin_users = [("Themis", "themis", "1"), ("Ilias", "ilias", "2"), ("Maria", "maria", "3")]
insert_user = "INSERT INTO users VALUES (?, ?, ?)"
cursor.executemany(insert_user, admin_users)
connection.commit()
connection.close()
