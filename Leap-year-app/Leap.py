from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def leap_year():
    result = "Enter a year"

    if request.method == 'POST':
        year = int(request.form['year'])

        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            result = str(year) + " is a Leap Year"
        else:
            result = str(year) + " is NOT a Leap Year"

    return f"""
    <html>
    <body>
        <h2>Leap Year Checker</h2>

        <form method="post">
            Enter Year:
            <input type="text" name="year" required>
            <input type="submit" value="Check">
        </form>

        <h3>{result}</h3>
    </body>
    </html>
    """


if __name__ == '__main__':
    app.run(debug=True)
