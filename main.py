import sqlite3

# creates a database connection
conn = sqlite3.connect(':memory:')

# creates a cursor object
curr = conn.cursor()

# creates a user table
curr.execute("CREATE TABLE user (username, age)")

# insert values into the table
curr.execute(
    """
        INSERT INTO user VALUES
            ('hamdi4-beep', 27)
    """
)

# commits the changes to the database
conn.commit()

res = curr.execute("SELECT username, age FROM user")

# retreives values from the database
username, age = res.fetchone()
print(f'{username} is {age} years old!')

conn.close()