# 서드파티
from flask import Flask, request, jsonify

# 프로젝트
import myopslib

app = Flask(__name__)


@app.route("/")
def home():
    return "<h3>텐서플로 자동차 연비 예측 플라스크 서비스 컨테이너</h3>"


@app.route("/hello")
def hello():
    return "hello ml"


@app.route("/predict", methods=["POST"])
def predict():
    """
    Input sample:
    {
        "Cylinders": 8,
        "Displacement": 390.0,
        "Horsepower": 190,
        "Weight": 3850,
        "Acceleration": 8.5,
        "ModelYear": 70,
        "Country": "USA",
    }

    Output sample:
    {
        "MPG": [ 16.075947 ]
    }
    """
    prediction = myopslib.predict(request.json)
    return jsonify({"MPG": prediction})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
