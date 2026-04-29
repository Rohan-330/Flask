from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Use URL: /largest/5/10/3/8/20"

@app.route('/largest/<int:a>/<int:b>/<int:c>/<int:d>/<int:e>')
def largest(a, b, c, d, e):
    return f"Largest Number: {max(a,b,c,d,e)}"

app.run()
