from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def even_numbers():
    result = ""

    if request.method == 'POST':
        n = int(request.form['n'])
        result = "Even Numbers:<br>"
        for i in range(2, 2*n + 1, 2):
            result += str(i) + " "

    return f"""
    <html>
    <body>
        <h2>Generate N Even Numbers</h2>

        <form method="post">
            Enter N:
            <input type="text" name="n" required><br><br>
            <input type="submit" value="Generate">
        </form>

        <h3>{result}</h3>
    </body>
    </html>
    """

app.run()          
