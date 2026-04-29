from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Use URL: /greet/name"

@app.route('/greet/<name>')
def greet(name):
    return "Hello " + name

if __name__ == '__main__':
    app.run(debug=True)
