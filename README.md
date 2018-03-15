# Pratical Python Project

## Overview

#### What is the purpose of this web app?

This is a quiz game that will generate a riddle for the user to work out.


#### What does it do?

The user will submit answers for what they thing the answer of the riddle is.

If they guess correctly, they'll progress to the next one. If they guess incorrectly, they'll can guess again.

#### How does it work?

For each riddle, if the user submits the correct answer for the riddle on their first attempt, they'll score 5 points and progress to the next answer.

If they guess incorrectly, they'll lose a point from the points that they can win that round.

Each guess would take away another possible mark until they get to 0 which will then take them to the next riddle.

After they've reached and answered the final riddle, their final score will submit to the scoreboard.

## To initilise and edit

1. Download Python 3: (http://www.python.org/download/)
2. Create a new directory to store the project 
``` $ mkdir riddle_me_this ```
``` $ cd riddle_me_this ```
3. Clone the repository 
``` $ git clone <https://github.com/DeanFlint/riddle-me-this.git>```
4. After you've that you'll need to make sure that you have **npm** installed. You can get **npm** by installing Node from [here](https://nodejs.org/en/)
``` $ npm install ```
``` $ npm start ```
5. Create and activate your virtual env:
``` $ python3 -m venv env ```
``` $ source env/bin/activate ```
6. Install Flask with pip:
``` (env)$ pip install flask==0.12.2 ```
7. Run the python file:
``` python3 app.py ```

## Features
#### Existing Features
- Username form
- A scoreboard
- Riddle-image generator

## Tech Used
#### Some of the tech used includes:
- **Flask** A Python based micro-framework used to serve the data from the server to the web based interface.
- **Bootstrap 4** I used **Bootstrap** to give my project a simple, responsive layout.
