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

1. Open up GITBASH
2. Use ls to navigate to your working directory
3. Type: npm install
4. Type: npm start

## Features
#### Existing Features
#### Features Left to Implement
- Username form
- A scoreboard
- Riddle-image generator

## Tech Used
#### Some of the tech used includes:
- **Flask** A Python based micro-framework used to serve the data from the server to the web based interface.
- **Bootstrap 4** I used **Bootstrap** to give my project a simple, responsive layout.

## Contributing
#### Getting the code up and running
1. Firstly you will need to clone this repository by running the ```git clone <https://github.com/DeanFlint/riddle-me-this.git>``` command
2. After you've that you'll need to make sure that you have **npm** installed. You can get **npm** by installing Node from [here](https://nodejs.org/en/)
3. Once **npm** , you'll need to install all of the dependencies in *package.json*.
```
npm install
```
4. After those dependencies have been installed you'll need to make sure that you have **http-server** installed. You can install this by running the following: ```npm install -g http-server # this also may require sudo on Mac/Linux```
5. Once **http-server** is installed run ```http-server -c-1```
6. The project will now run on [localhost](http://127.0.0.1:8080)
7. Make changes to the code and if you think it belongs in here then just submit a pull request