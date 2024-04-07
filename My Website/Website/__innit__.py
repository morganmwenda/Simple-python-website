from flask import Flask
#creating the flask app
def create_app():
    app=Flask(__name__)
    app.config['SECRET KEY']='mmk'

    return app

#after import the app to main.py