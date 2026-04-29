from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def samallest():
    result = ""

    if request.method == 'POST':
        nums = request.form['numbers']          
        num_list = list(map(int, nums.split())) 
        result = f"Smallest Number: {min(num_list)}"

    return f"""
    <html>
    <body>
        <h2>Find Smallest Number</h2>

        <form method="post">
            Enter numbers (space separated):
            <input type="text" name="numbers" required>
            <input type="submit" value="Find">
        </form>

        <h3>{result}</h3>
    </body>
    </html>
    """

app.run()
