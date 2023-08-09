# flask tutorial 1

# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return 'hi, this is my first flask tutorial! :)<h1>HI</h1>'
# if __name__ == '__main__':
#     app.run()

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'hi, this is my first flask tutorial! <h1>HI</h1>'

if __name__ == '__main__':
    app.run()