from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def multiply():
    result = ""

    if request.method == 'POST':
        a1 = int(request.form['a1'])
        a2 = int(request.form['a2'])
        a3 = int(request.form['a3'])
        a4 = int(request.form['a4'])

        b1 = int(request.form['b1'])
        b2 = int(request.form['b2'])
        b3 = int(request.form['b3'])
        b4 = int(request.form['b4'])

        result = f"""
        Result Matrix:<br>
        {a1*b1 + a2*b3} {a1*b2 + a2*b4}<br>
        {a3*b1 + a4*b3} {a3*b2 + a4*b4}
        """

    return f"""
    <html>
    <body>
        <h2>Matrix Multiplication (2×2)</h2>

        <form method="post">
            Matrix A:<br>
            <input name="a1" required>
            <input name="a2" required><br>
            <input name="a3" required>
            <input name="a4" required><br><br>

            Matrix B:<br>
            <input name="b1" required>
            <input name="b2" required><br>
            <input name="b3" required>
            <input name="b4" required><br><br>

            <input type="submit" value="Multiply">
        </form>

        <h3>{result}</h3>
    </body>
    </html>
    """

app.run()
