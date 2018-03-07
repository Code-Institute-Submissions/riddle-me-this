import os
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

def write_to_file(filename, data):
    """ Handle the process of writing data to a file """
    with open(filename, "a") as file:
        file.writelines(data)
    
@app.route('/challenge', methods=["GET", "POST"])
def challenge():
    """Handle POST request"""
    if request.method == "POST":
        write_to_file("data/users.txt", request.form["username"] + "\n")
        return redirect(request.form["username"])
    return render_template("challenge.html")
    
@app.route('/challenge/<username>')
def user(username):
    """Display chat messages"""
    return render_template("scoreboard.html", 
                                username=username)
    
@app.route('/scoreboard')
def scoreboard():
    return render_template("scoreboard.html")


app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)