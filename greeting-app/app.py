from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Welcome to the world of Information Technology!'

if __name__ == '__main__':
    app.run(debug=True)
