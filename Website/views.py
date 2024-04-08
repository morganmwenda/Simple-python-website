from flask import Blueprint #shows the blueprint of the website

views = Blueprint('views',__name__)

@views.route('/')  # put the url for the end point here

def home():
    return "<h1> test </h1>"
