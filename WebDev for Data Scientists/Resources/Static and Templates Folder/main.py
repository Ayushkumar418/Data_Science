from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, Harry!</p>"


@app.route("/about")
def about():
    return render_template("index.html")


@app.route("/contact")
def contact():
    return "<p>Hello, I am contact page!</p>"


app.run(debug=True)