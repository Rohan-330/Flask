from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def marks_app():
    message = "Enter your marks below"

    if request.method == 'POST':
        marks = request.form['marks']
        message = "Hello Student! Your marks are " + marks

    return f"""
    <html>
    <body>
        <h2>Marks Submission Form</h2>

        <form method="post">
            Enter Your Marks:
            <input type="text" name="marks" required>
            <input type="submit" value="Submit">
        </form>

        <h3>{message}</h3>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
