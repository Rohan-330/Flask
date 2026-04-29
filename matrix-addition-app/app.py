from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Use URL: /add/a11/a12/a21/a22/b11/b12/b21/b22"

@app.route('/add/<int:a11>/<int:a12>/<int:a21>/<int:a22>/<int:b11>/<int:b12>/<int:b21>/<int:b22>')
def add_matrix(a11, a12, a21, a22, b11, b12, b21, b22):
    c11 = a11 + b11
    c12 = a12 + b12
    c21 = a21 + b21
    c22 = a22 + b22

    return f"""
    Matrix A:<br>
    {a11} {a12}<br>
    {a21} {a22}<br><br>

    Matrix B:<br>
    {b11} {b12}<br>
    {b21} {b22}<br><br>

    Result Matrix:<br>
    {c11} {c12}<br>
    {c21} {c22}
    """

app.run()
