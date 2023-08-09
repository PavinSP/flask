from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'hi this is my first tutorial<h1>HELLO</h1>' + ('<h1>HELLO</h1>')
if __name__ == '__main__':
    app.run()