from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def concat():
    result = ""

    if request.method == 'POST':
        str1 = request.form['str1']
        str2 = request.form['str2']
        result = str1 + str2

    return f"""
    <html>
    <head>
        <title>String Concatenation</title>
    </head>
    <body>
        <h2>String Concatenation</h2>

        <form method="post">
            Enter First String:
            <input type="text" name="str1"><br><br>

            Enter Second String:
            <input type="text" name="str2"><br><br>

            <input type="submit" value="Concatenate">
        </form>

        <h3>Concatenated String: {result}</h3>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
