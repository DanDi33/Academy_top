import sqlite3


def db_init(nameDatabase):
    con = sqlite3.connect(f"{nameDatabase}.db")
    cursor = con.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        );
    """)
    return (cursor, con)


def register_user(username, password, cursor, con):
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        con.commit()
        return True
    except sqlite3.IntegrityError:
        return False


def auth_user(username, password, cursor, con):
    cursor.execute("SELECT * FROM users WHERE username = ? and password = ?", (username, password))
    user = cursor.fetchone()
    # if user is not None:
    #     return user
    # else:
    #     return None
    return user is not None


if __name__ == "__main__":
    cursor, con = db_init("users")
    # register_user("Tom", "123456", cursor, con)
    print(auth_user("Tom", "123456", cursor, con))

