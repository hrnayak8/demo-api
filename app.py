from flask import Flask, render_template, request
import tensorflow as tf
import cv2
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", data="hi")

@app.route('/prediction', methods=["POST"])
def prediction():

    return "wellcome to prediction"

if __name__ == "__main__":
    app.run(debug=True)
