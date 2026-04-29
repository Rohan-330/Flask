from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = ""

    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']

        if operation == "add":
            result = num1 + num2
        elif operation == "sub":
            result = num1 - num2
        elif operation == "mul":
            result = num1 * num2
        elif operation == "div":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Cannot divide by zero"

    return f"""
    <html>
    <body>
        <h2>Simple Calculator Web Service</h2>

        <form method="post">
            Enter First Number:
            <input type="text" name="num1" required><br><br>

            Enter Second Number:
            <input type="text" name="num2" required><br><br>

            Select Operation:
            <select name="operation">
                <option value="add">Addition</option>
                <option value="sub">Subtraction</option>
                <option value="mul">Multiplication</option>
                <option value="div">Division</option>
            </select><br><br>

            <input type="submit" value="Calculate">
        </form>

        <h3>Result: {result}</h3>
    </body>
    </html>
    """
if __name__ == '__main__':
    app.run(debug=True)
