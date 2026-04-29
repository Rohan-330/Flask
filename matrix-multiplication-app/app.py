from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Use URL: /multiply/a1/a2/a3/a4/b1/b2/b3/b4"

@app.route('/multiply/<int:a1>/<int:a2>/<int:a3>/<int:a4>/<int:b1>/<int:b2>/<int:b3>/<int:b4>')
def multiply(a1, a2, a3, a4, b1, b2, b3, b4):
    c1 = a1*b1 + a2*b3
    c2 = a1*b2 + a2*b4
    c3 = a3*b1 + a4*b3
    c4 = a3*b2 + a4*b4

    return f"""
    Matrix A:<br>
    {a1} {a2}<br>
    {a3} {a4}<br><br>

    Matrix B:<br>
    {b1} {b2}<br>
    {b3} {b4}<br><br>

    Result Matrix:<br>
    {c1} {c2}<br>
    {c3} {c4}
    """

app.run()
