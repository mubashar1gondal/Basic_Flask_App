from app import app
from flask import render_template, Flask, redirect, url_for, request

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template('login.html')

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"


@app.route('/blog')
def blog():
    return "This is the blog page"

if __name__ == "__main__":
    app.run(debug=True)
    