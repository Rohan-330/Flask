from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Use URL: /concat/string1/string2"

@app.route('/concat/<str1>/<str2>')
def concat(str1, str2):
    return "Concatenated String: " + str1 + str2

if __name__ == '__main__':
    app.run(debug=True)
