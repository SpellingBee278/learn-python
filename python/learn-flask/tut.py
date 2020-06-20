
# import flask framework, this tutorial series was by techwithtim

from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)
FLASK_DEBUG = 1


@app.route("/<name>")
def home(name):
    return render_template("index.html", content=["Stop", "joe", "Baquaaas"])


if __name__ == "__main__":
    app.run()

