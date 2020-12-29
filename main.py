from flask import Flask, Response

app = Flask(__name__)

body = {'Key': 'Value'}

@app.route("/")
def print_hi():
    return body, 200


@app.route("/hello")
def new():
    return body, 201

if __name__ == '__main__':
    app.run()
