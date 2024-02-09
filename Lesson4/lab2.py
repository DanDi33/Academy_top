import sqlite3
import bcrypt
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

con = sqlite3.connect(f"users.db")
cursor = con.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    );
""")


# def db_init(nameDatabase):
#     con = sqlite3.connect(f"{nameDatabase}.db")
#     cursor = con.cursor()
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS users (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             username TEXT NOT NULL UNIQUE,
#             password TEXT NOT NULL
#         );
#     """)
#     return (cursor, con)


def register_user(username, password, cursor, con):
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                       (username, hashed_password.decode("utf-8")))
        con.commit()
        return True
    except sqlite3.IntegrityError:
        return False


def auth_user(username, password, cursor, con):
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    # if user is not None:
    #     return user
    # else:
    #     return None
    if user and bcrypt.checkpw(password.encode("utf-8"), user[2].encode('utf-8')):

        return True
    else:
        return False
    # return user is not None


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if register_user(username, password):
            return url_for('/login')
        else:
            return render_template('register.html', error="Ошибка")
    else:
        return render_template('register.html')


if __name__ == "__main__":
    app.run(debug=True)
    # cursor, con = db_init("users")
    # # register_user("Tim", "123456", cursor, con)
    # print(auth_user("Tim", "123456", cursor, con))
