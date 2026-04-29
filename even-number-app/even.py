from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Use URL: /even/n"

@app.route('/even/<int:n>')
def even(n):
    result = "Even Numbers:<br>"
    for i in range(2, 2*n + 1, 2):
        print(i)
        result += str(i) + " "
        print(result)
    return result

app.run()
