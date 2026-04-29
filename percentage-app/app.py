from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def percentage():
    message = "Enter your percentage"

    if request.method == 'POST':
        percent = request.form['percent']
        message = "Hello Student! Your percentage is " + percent + "%"

    return f"""
    <html>
    <body>
        <h2>Percentage Submission Form</h2>

        <form method="post">
            Enter Your Percentage:
            <input type="text" name="percent" required>
            <input type="submit" value="Submit">
        </form>

        <h3>{message}</h3>
    </body>
    </html>
    """

app.run()
