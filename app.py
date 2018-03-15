import os
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
app.config.from_object(__name__)

def riddle_answers():
    answers = []
    with open("data/answers.txt", "r") as file:
        lines = file.read().splitlines()
    for line in lines:
        answers.append(line)
    return answers

def clear_answers():
    """ Clear the guesses.txt file"""
    with open("data/guesses.txt", "w"):
        return
    
def write_to_file(filename, data):
    """ Handle the process of writing data to a file """
    with open(filename, "a") as file:
        file.writelines(data)
        
def get_all_attempts():
    """Get all of the messages and seperate them by a `br` """
    attempts = []
    with open("data/guesses.txt", "r") as incorrect_attempts:
        attempts = incorrect_attempts.readlines()
    return attempts

@app.route('/', methods=["GET", "POST"])
def index():
    """Handle POST request"""
    if request.method == "POST":
        write_to_file("data/users.txt", request.form["username"] + "\n")
        return redirect(request.form["username"])
    return render_template("index.html")

@app.route('/<username>', methods=["GET", "POST"])
def user(username):
    attempts = get_all_attempts()
    attempts_num = len(attempts)
    if request.method == "POST":
        write_to_file("data/guesses.txt", request.form["answer"] + "\n")
        guess = request.form["answer"]
        answers = riddle_answers()
        username=username
        if answers[0] == guess:
            score = 5 - attempts_num
            clear_answers()
            return redirect(url_for('riddle2', username=username))
        else:
            if attempts_num > 4:
                return redirect(url_for('riddle2', username=username))
            else:
                return render_template("riddle1.html", username=username, attempts=attempts, attempts_num=attempts_num)
    return render_template("riddle1.html", username=username)

@app.route('/<username>/riddle2', methods=["GET", "POST"])
def riddle2(username):
    if request.method == "POST":
        write_to_file("data/guesses.txt", request.form["answer"] + "\n")
        guess = request.form["answer"]
        answers = riddle_answers()
        if answers[1] == guess:
            clear_answers()
            return redirect(url_for('riddle3', username=username)) 
        else:
            return render_template("riddle2.html", username=username)    
    return render_template("riddle2.html", username=username)  

@app.route('/<username>/riddle3', methods=["GET", "POST"])    
def riddle3(username):
    if request.method == "POST":
        write_to_file("data/guesses.txt", request.form["answer"] + "\n")
        guess = request.form["answer"]
        answers = riddle_answers()
        if answers[2] == guess:
            clear_answers()
            return redirect(url_for('riddle4', username=username))
        else:
            return render_template("riddle3.html", username=username)
    return render_template("riddle3.html", username=username)
    
@app.route('/<username>/riddle4', methods=["GET", "POST"])    
def riddle4(username):
    if request.method == "POST":
        write_to_file("data/guesses.txt", request.form["answer"] + "\n")
        guess = request.form["answer"]
        answers = riddle_answers()
        if answers[3] == guess:
            clear_answers()
            return redirect(url_for('riddle5', username=username))
        else:
            return render_template("riddle4.html", username=username)
    return render_template("riddle5.html", username=username)
    
@app.route('/<username>/riddle5', methods=["GET", "POST"])    
def riddle5(username):
    if request.method == "POST":
        write_to_file("data/guesses.txt", request.form["answer"] + "\n")
        guess = request.form["answer"]
        answers = riddle_answers()
        if answers[4] == guess:
            clear_answers()
            return render_template("riddle6.html", username=username)
        else:
            return render_template("riddle3.html", username=username)
    return render_template("riddle3.html", username=username)
    
@app.route('/scoreboard')
def scoreboard():
    return render_template("scoreboard.html")


app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)