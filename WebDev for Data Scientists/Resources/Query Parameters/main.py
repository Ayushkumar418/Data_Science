from flask import Flask, render_template, request

app = Flask(__name__)

app.secret_key = 'your_secret_key'

@app.route("/")
def hello_world(): 
    name  = request.args.get("name", default="Unnamed")
    lang  = request.args.get("lang")
    print(name, lang)
    return render_template("index.html", lang=lang, name=name) 

app.run(debug=True)