from flask import Flask, jsonify, request
from src import load_model

"""
Mlflow deployment app
"""

app = Flask(__name__)

@app.route("/")
def hello_world():
    """
    Simple heartbeat
    """
    return jsonify(hello="world")


@app.route("/predict", methods = ['POST'])
def predict() -> str:
    """
    Predict on an incoming data
    """

    # convert request data to json
    data = request.json
    # predict results
    result = load_model.predict(data)

    # return jsonified results
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0')