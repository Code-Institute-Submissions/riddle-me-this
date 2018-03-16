import os
from flask import Flask, redirect, render_template, request, url_for
from operator import itemgetter

app = Flask(__name__)
app.config.from_object(__name__)

def riddle_answers():
    """ Create an array of the riddle answers """
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
  
    
def num_of_attempts():
    """ The number of attempts made by the user on the current riddle """
    attempts = get_all_attempts()
    return len(attempts);
 
    
def attempts_rem():
    """ Return the number of attempts remaining """
    rem_attempts = 5 - num_of_attempts()
    return rem_attempts;


def add_to_score():
    """ Add the score award during the round depeneding on how many turns it took to answer correctly """
    round_score = 6 - num_of_attempts()
    return round_score;
  
    
def final_score(username, score):
    if username != "" and score != "":
        with open("data/scores.txt", "a") as file:
            if int(score) > 0 and int(score) < 10:
                score = "0" + str(score)
            file.writelines(str(score) + "\n")
            file.writelines(str(username) + "\n")
    else:
        return
  
        
def get_scores():
    usernames = []
    scores = []
    
    with open("data/scores.txt", "r") as file:
        lines = file.read().splitlines()
        
    for i, text in enumerate(lines):
        if i%2 ==0:
            scores.append(text)
        else:
            usernames.append(text)
    
    usernames_and_scores = zip(usernames, scores)
    usernames_and_scores.sort(key=itemgetter(1), reverse=True)
    return usernames_and_scores


@app.route('/', methods=["GET", "POST"])
def index():
    clear_answers()
    score = 0
    """Handle POST request"""
    if request.method == "POST":
        write_to_file("data/users.txt", request.form["username"] + "\n")
        username = request.form["username"]
        return redirect(url_for('user', username=username, score=score))
    return render_template("index.html")


@app.route('/<username>/riddle1/<int:score>', methods=["GET", "POST"])
def user(username, score):
    rem_attempts = 5
    if request.method == "POST":
        write_to_file("data/guesses.txt", request.form["answer"] + "\n")
        guess = request.form["answer"]
        answers = riddle_answers()
        if answers[0] == guess:
            score = score + add_to_score()
            clear_answers()
            return redirect(url_for('riddle2', username=username, score=score))
        else:
            if num_of_attempts() > 4:
                clear_answers()
                return redirect(url_for('riddle2', username=username, score=score))
            else:
                return render_template("riddle1.html", username=username, attempts=get_all_attempts(), rem_attempts=attempts_rem(), score=score)
    return render_template("riddle1.html", username=username, rem_attempts=rem_attempts, score=score)


@app.route('/<username>/riddle2/<int:score>', methods=["GET", "POST"])
def riddle2(username, score):
    rem_attempts = 5
    if request.method == "POST":
        write_to_file("data/guesses.txt", request.form["answer"] + "\n")
        guess = request.form["answer"]
        answers = riddle_answers()
        if answers[1] == guess:
            score = score + add_to_score()
            clear_answers()
            return redirect(url_for('riddle3', username=username, score=score))
        else:
            if num_of_attempts() > 4:
                clear_answers()
                return redirect(url_for('riddle3', username=username, score=score))
            else:
                return render_template("riddle2.html", username=username, attempts=get_all_attempts(), rem_attempts=attempts_rem(), score=score)
    return render_template("riddle2.html", username=username, rem_attempts=rem_attempts, score=score)


@app.route('/<username>/riddle3/<int:score>', methods=["GET", "POST"])
def riddle3(username, score):
    rem_attempts = 5
    if request.method == "POST":
        write_to_file("data/guesses.txt", request.form["answer"] + "\n")
        guess = request.form["answer"]
        answers = riddle_answers()
        if answers[2] == guess:
            score = score + add_to_score()
            clear_answers()
            return redirect(url_for('riddle4', username=username, score=score))
        else:
            if num_of_attempts() > 4:
                clear_answers()
                return redirect(url_for('riddle4', username=username, score=score))
            else:
                return render_template("riddle3.html", username=username, attempts=get_all_attempts(), rem_attempts=attempts_rem(), score=score)
    return render_template("riddle3.html", username=username, rem_attempts=rem_attempts, score=score)


@app.route('/<username>/riddle4/<int:score>', methods=["GET", "POST"])
def riddle4(username, score):
    rem_attempts = 5
    if request.method == "POST":
        write_to_file("data/guesses.txt", request.form["answer"] + "\n")
        guess = request.form["answer"]
        answers = riddle_answers()
        if answers[3] == guess:
            score = score + add_to_score()
            clear_answers()
            return redirect(url_for('riddle5', username=username, score=score))
        else:
            if num_of_attempts() > 4:
                clear_answers()
                return redirect(url_for('riddle5', username=username, score=score))
            else:
                return render_template("riddle4.html", username=username, attempts=get_all_attempts(), rem_attempts=attempts_rem(), score=score)
    return render_template("riddle4.html", username=username, rem_attempts=rem_attempts, score=score)
 
    
@app.route('/<username>/riddle5/<int:score>', methods=["GET", "POST"])
def riddle5(username, score):
    rem_attempts = 5
    if request.method == "POST":
        write_to_file("data/guesses.txt", request.form["answer"] + "\n")
        guess = request.form["answer"]
        answers = riddle_answers()
        if answers[4] == guess:
            score = score + add_to_score()
            clear_answers()
            final_score(username, score)
            return redirect(url_for('scoreboard'))
        else:
            if num_of_attempts() > 4:
                clear_answers()
                final_score(username, score)
                return redirect(url_for('scoreboard'))
            else:
                return render_template("riddle5.html", username=username, attempts=get_all_attempts(), rem_attempts=attempts_rem(), score=score)
    return render_template("riddle5.html", username=username, rem_attempts=rem_attempts, score=score)
    
    
@app.route('/scoreboard')
def scoreboard():
    usernames_and_scores = get_scores()
    return render_template("scoreboard.html", usernames_and_scores=usernames_and_scores)


app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)