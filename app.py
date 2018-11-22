from flask import Flask
from flask import render_template, request
from database import *
app = Flask(__name__)

@app.route('/')
def hello_world():
    cats = get_all_cats()
    return render_template("home.html", cats=cats)
if __name__ == '__main__':
    app.run(debug=True)

