from flask import Blueprint #shows the blueprint of the website

auth = Blueprint('auth',__name__)

@auth.route('/login')  # put the url for the end point here

def login():
    return "<h1> test </h1>"