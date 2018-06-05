# Riddle Me This 

[![Build Status](https://travis-ci.org/DeanFlint/riddle-me-this.svg?branch=master)](https://travis-ci.org/DeanFlint/riddle-me-this)

## Getting Started

This logic-driven web application is a quiz game that will generate a riddle for the user to work out.

The user will submit answers for what they think the answer of the riddle is. If they guess correctly, 
they'll progress to the next one. If they guess incorrectly, they'll can guess again.

For each riddle, if the user submits the correct answer for the riddle on their first attempt, 
they'll score 5 points and progress to the next answer. If they guess incorrectly, they'll lose a 
point from the points that they can win that round. Each guess would take away another possible mark 
until they get to 0 which will then take them to the next riddle. After they've reached and answered 
the final riddle, their final score will submit to the scoreboard.

This has been written in Python(Flask), HTML, CSS and JavaScript. 

## Prerequisites

The list of tech used includes:

- [Flask](http://flask.pocoo.org/)
    - I used **Flask** (which is a python microframework) to render pages and manage the functionality.
- [Bootstrap](http://getbootstrap.com/)
    - I used **Bootstrap** to give my project a simple, responsive layout
- [npm](https://www.npmjs.com/)
    - I used **npm** to help manage some of the dependencies in our application
- [gulp](https://gulpjs.com/)
    - **Gulp** is used to manage the tasks of running the scss and moving files from Node Modules to my project folders.
- [font-awesome](http://fontawesome.io/)
    - I used **font-awesome** to include images for icons.
- [Google Fonts](https://fonts.google.com/) 
    - **Google Fonts** is used to style the text in my site.

## WireFrame

Click [here](wireframe.pdf) to view the wireframe of this project.

## To initilise and edit

1. Download Python 3: (http://www.python.org/download/)

2. Clone the repository 

``` $ git clone https://github.com/DeanFlint/riddle-me-this.git```

3. Move into the folder

``` cd riddle-me-this ```

4. After you've that you'll need to make sure that you have **npm** installed. You can get **npm** by installing Node from [here](https://nodejs.org/en/)

``` $ npm install ```

``` $ npm start ```


5. Create and activate your virtual env:

``` $ python -m venv env ```

``` $ source env/Scripts/activate ```

6. Install requirements with pip:

``` (env)$ pip install -r requirements.txt ```

7. Open app.py using a text editor to amend the port number on the bottom line, for example:

``` app.run(host=os.getenv('IP'), port=5005, debug=True) ```

8. Run the python file:

``` python3 app.py ```

## Running the tests

### Break down into end to end tests

Explain what these tests test and why

```
TO DO
```


## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Dean Flint** - *Initial work* - [Dean Flint](https://github.com/DeanFlint)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* The good people at CodeInstitute!

* Derek Hyland
