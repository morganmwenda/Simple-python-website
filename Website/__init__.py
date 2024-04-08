from flask import Flask
#creating the flask app
def create_app():
    app=Flask(__name__)
    app.config['SECRET KEY']='mmk'

    from .views import views #importing blueprints
    from .auth import auth

    #register blue prints
    app.register_blueprint(views,url_prefix='/') #prefix is what is defined as the fucnction
    app.register_blueprint(auth,url_prefix='/')


    return app

#after import the app to main.py