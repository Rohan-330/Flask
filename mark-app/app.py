from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Use URL: /marks/value"

@app.route('/marks/<marks>')
def marks(marks):
    return "Hello Student! Your marks are " + marks

if __name__ == '__main__':
    app.run(debug=True)
