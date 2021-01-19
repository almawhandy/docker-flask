from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Ciao a tutti"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
