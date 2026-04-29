from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def matrix_add():
    result = ""

    if request.method == 'POST':
        a11 = int(request.form['a11'])
        a12 = int(request.form['a12'])
        a21 = int(request.form['a21'])
        a22 = int(request.form['a22'])

        b11 = int(request.form['b11'])
        b12 = int(request.form['b12'])
        b21 = int(request.form['b21'])
        b22 = int(request.form['b22'])

        c11 = a11 + b11
        c12 = a12 + b12
        c21 = a21 + b21
        c22 = a22 + b22

        result = f"""
        Result Matrix:<br>
        {c11} {c12}<br>
        {c21} {c22}
        """

    return f"""
    <html>
    <body>
        <h2>Addition of Two Matrices (2x2)</h2>

        <form method="post">
            Matrix A:<br>
            <input type="text" name="a11" required>
            <input type="text" name="a12" required><br>
            <input type="text" name="a21" required>
            <input type="text" name="a22" required><br><br>

            Matrix B:<br>
            <input type="text" name="b11" required>
            <input type="text" name="b12" required><br>
            <input type="text" name="b21" required>
            <input type="text" name="b22" required><br><br>

            <input type="submit" value="Add Matrices">
        </form>

        <h3>{result}</h3>
    </body>
    </html>
    """

app.run()
