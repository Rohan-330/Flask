from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Use URL: /percentage/value"

@app.route('/percentage/<percent>')
def percentage(percent):
    return "Hello Student! Your percentage is " + percent + "%"


if __name__ == '__main__':
    app.run(debug=True)
