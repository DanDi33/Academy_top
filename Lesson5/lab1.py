from flask import Flask, render_template, request, flash, session, redirect, url_for

app = Flask(__name__)
app.config["SECRET_KEY"] = "qwerty1234567890"
menu = [{"name": "Главная", "url": "/"},
        {"name": "О нас", "url": "/about"},
        {"name": "Обратная связь", "url": "/contact"}]


@app.route("/")
@app.route('/index')
def index():
    # print(url_for('index'))
    return render_template("index.html", menu=menu, title="Главная")


@app.route("/about")
def about():
    # print(url_for('about'))
    return render_template("about.html", menu=menu, title="О компании")


@app.route("/profile/<path:username>")
def profile(username):
    # print(url_for('profile', username='11'))
    return f"Пользователь -- {username}"


@app.route("/contact", methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        if len(request.form['name']) >= 2:
            flash('Сообщение доставлено', category="success")
        else:
            flash('Ошибка доставки', category="error")
    return render_template("contact.html", menu=menu, title="Обратная связь")


@app.errorhandler(404)
def pageNorFound(error):
    return render_template("page404.html", menu=menu, title="Страница не найдена")


@app.route("/login", methods=['POST', 'GET'])
def login():
    # session['userLogged'] = "123123"
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session["userLogged"]))
    elif request.method == "POST":
        if request.form['name'] == "Test" and request.form['psw'] == "123":
            session['userLogged'] = request.form['name']
            return redirect(url_for('profile', username=session["userLogged"]))
    # print(session)
    return render_template("login.html", menu=menu, title="Авторизация")


if __name__ == "__main__":
    app.run(debug=True)
