from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", data="hi")

@app.route('/prediction', methods=["POST"])
def prediction():

    return "wellcome to prediction"

if __name__ == "__main__":
    app.run(debug=True)
