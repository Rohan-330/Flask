from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def greet():
    name = ""

    if request.method == 'POST':
        name = request.form['username']

    return f"""
    <html>
    <body>
        <h2>Greeting Application</h2>

        <form method="post">
            Enter Your Name:
            <input type="text" name="username">
            <input type="submit" value="Submit">
        </form>

        <h3>Hello {name}</h3>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
