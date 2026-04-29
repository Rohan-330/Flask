from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Use URL: /swap/a/b"

@app.route('/swap/<int:a>/<int:b>')
def swap(a, b):
    # return "Before Swap: a = " + str(a) + ", b = " + str(b) + \
    #        "<br>After Swap: a = " + str(b) + ", b = " + str(a)

    return f"Before Swap: a = {a}, b = {b}<br>After Swap: a = {b}, b = {a}"

app.run()
