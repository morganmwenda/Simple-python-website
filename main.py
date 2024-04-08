#the  __innit__.py in the folder website makes the entire folder a python package, allowing importing
from Website import create_app


app = create_app()

if __name__ == '__main__': #runs the app only when we run main.py
    app.run(debug=True) #debug=True reloads the website after changes are made


