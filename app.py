from flask import Flask
from flask import render_template, request
from database import * 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR-VERY-SECRET-SHHH'

@app.route('/')
def catbook_home():
    cats = get_all_cats()
    return render_template("home.html", cats=cats)
    
@app.route('/cats/<int:id>')
def name_route(id):
    cat=get_cat(id)
    print("---")
    print(cat)
    return render_template("cat.html", cat=cat)


@app.route("/response", methods=['GET','POST'])
def addcat():
    if request.method == 'GET' :
        return render_template("response.html")
    else:
        name=request.form['firstname']
        create_cat(name,0)
        cats = get_all_cats()
        return render_template('home.html',
        cats = cats)

@app.route("/vote", methods=['GET','POST'])
def voteforcat():
    if request.method == 'GET' :
        cats = get_all_cats()
        return render_template("vote.html",
        cats = cats)
    
    else:
        vote += 1
        cats = get_all_cats()
        return render_template('home.html',
        cats = cats)

if __name__ == '__main__':
   app.run(debug = True)
