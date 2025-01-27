import sqlite3

conn = sqlite3.connect(':memory:')
curr = conn.cursor()

curr.execute("CREATE TABLE user (username, id)")

curr.execute(
    """
        INSERT INTO user VALUES
            ('hamdi4-beep', 8)
    """
)

conn.commit()

res = curr.execute("SELECT username, id FROM user")
print(res.fetchall())