from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def swap():
    result = "Enter two numbers"

    if request.method == 'POST':
        a = request.form['a']
        b = request.form['b']
        result = f"Before Swap: a = {a}, b = {b}<br>After Swap: a = {b}, b = {a}"

    return f"""
    <html>
    <body>
        <h2>Swap Two Numbers</h2>

        <form method="post">
            Enter First Number:
            <input type="text" name="a" required><br><br>

            Enter Second Number:
            <input type="text" name="b" required><br><br>

            <input type="submit" value="Swap">
        </form>

        <h3>{result}</h3>
    </body>
    </html>
    """

app.run()
