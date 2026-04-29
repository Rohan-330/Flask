from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Use URL: /odd/n"

@app.route('/odd/<int:n>')
def odd(n):
    result = "Odd Numbers:<br>"
    for i in range(1, 2*n, 2):
        result += str(i) + " "
    return result

app.run()
