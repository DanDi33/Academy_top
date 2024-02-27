import datetime
import json

from flask import Flask, render_template, make_response, redirect, url_for, request, session

app = Flask(__name__)
app.config["SECRET_KEY"] = "dgweddfgdfgdfgdfg"

app.permanent_session_lifetime = datetime.timedelta(days=10)
menu = [
    {"title": "Main", "url": '/'}
]


@app.route("/")
def index():
    session.permanent = True
    if "visits" in session:
        session['visits'] = session.get("visits") + 1
    else:
        session["visits"] = 1
    return f"<h1>Main page</h1> visits {session['visits']}"

    # return "<h1>Main Page</h1>"

    # data = '{"name":"John Smith"}'
    # res = make_response(data)
    # res.headers['Content-Type'] = "application/json"
    # return res, 201

    # return ("<h1>Hello world</h1>", 200)

    # audio = None
    # with app.open_resource(app.root_path + "/static/audio/sound-1.mp3", mode="rb") as f:
    #     audio = f.read()    #
    # if audio is None:
    #     return "None audio"
    # res = make_response(audio)
    # res.headers['Content-Type'] = "audio/mp4"
    # res.headers["server"] = "flask-test"
    # return res

    # contex = render_template("index.html",menu=menu,posts=[])
    # res = make_response(contex)
    # res.headers["Content-Type"] = "text/plain"
    # return res


@app.route("/login")
def login():
    log = ""
    if request.cookies.get("logged"):
        log = request.cookies.get("logged")
    res = make_response(f"<h1>Форма авторизации</h1> logged: {log}")
    res.set_cookie("logged", "yes", 30 * 24 * 3600)
    return res


@app.route("/logout")
def logout():
    res = make_response("Вы больше не авторизованы")
    res.set_cookie("logged", "")
    return res


@app.route("/transfer")
def transfer():
    return (redirect(url_for("index")), 301)


# 0

# @app.before_request
# def before_request():
#     print("before_request")
#
# @app.after_request
# def after_request(response):
#     print("after_request")
#     return response
#
# @app.teardown_request
# def teardown_request(response):
#     print("teardown_request")
#     return response


if __name__ == '__main__':
    app.run(debug=True)
