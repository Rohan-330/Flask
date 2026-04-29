from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Use URL: /leap/year"

@app.route('/leap/<int:year>')
def leap(year):
    if year % 4 == 0:
        return str(year) + " is a Leap Year"
    else:
        return str(year) + " is NOT a Leap Year"


if __name__ == '__main__':
    app.run(debug=True) 
