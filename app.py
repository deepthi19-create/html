from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, deepthi usn 1ga23cs036!</p>"
if __name__ == "__main__":
   app.run(host="0.0.0.0")
