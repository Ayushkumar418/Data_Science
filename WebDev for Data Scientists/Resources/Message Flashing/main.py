from flask import Flask, render_template, flash

app = Flask(__name__)

app.secret_key = 'your_secret_key'

@app.route("/")
def hello_world():
    flash("Thank you")
    return render_template("index.html")

@app.route("/about")
def about():
    flash("Thanks for visiting about page")
    return render_template("about.html")

app.run(debug=True)