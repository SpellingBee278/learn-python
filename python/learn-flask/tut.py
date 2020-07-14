# import flask framework, this tutorial series was by techwithtim
from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
import sqlalchemy as sql

app = Flask(__name__)
app.secret_key = "sec_key"
app.permanent_session_lifetime = timedelta(days=1)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        flash("Login Successful!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already Logged In!")
            return redirect(url_for("user"))
        return render_template("login.html")


@app.route("/user", methods=["POST", "GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]

        # return f"<h1>{user}</h1>"
        return render_template("user.html", email=email)
        # return render_template(url_for("user.html", user=user))
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    if "user" in session:
        user = session["user"]
        flash(f"You have been logged out, {user}!", "info")
        session.pop("user", None)
        return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)

