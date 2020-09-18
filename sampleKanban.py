from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Hello world", 200
    # return render_template("welcome.html", cards=db)