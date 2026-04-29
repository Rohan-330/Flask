from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def odd_numbers():
    result = ""

    if request.method == 'POST':
        n = int(request.form['n'])
        result = "Odd Numbers:<br>"
        for i in range(1, 2*n, 2):
            result += str(i) + " "

    return f"""
    <html>
    <body>
        <h2>Generate N Odd Numbers</h2>

        <form method="post">
            Enter N:
            <input type="text" name="n" required>
            <input type="submit" value="Generate">
        </form>

        <h3>{result}</h3>
    </body>
    </html>
    """

app.run()
