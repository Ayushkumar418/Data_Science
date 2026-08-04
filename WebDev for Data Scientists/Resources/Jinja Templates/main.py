from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    name = "Jill"
    language = "JavaScript"
    luckynos = [1, 5, 76, 86, 99, 100]
    footer = "<p> Copyright 2025  | All rights reserved</p>"
    return render_template("index.html", name=name, lang=language, lucky=luckynos, footer=footer)


app.run(debug=True)