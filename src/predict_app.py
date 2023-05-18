"""House price prediction service"""

from flask import Flask, request

app = Flask(__name__)


def get_model():
    """Build model and load weights from disk"""
    return sum


@app.route("/")
def home():
    """Dummy service"""
    f_1 = request.args.get("f1")
    f_2 = request.args.get("f2")
    f_3 = request.args.get("f3")
    f_1, f_2, f_3 = int(f_1), int(f_2), int(f_3)
    model = get_model()
    result = model([f_1, f_2, f_3])
    return str(result)


if __name__ == "__main__":
    app.run()
