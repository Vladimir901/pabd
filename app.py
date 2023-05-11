# app.py

from flask import Flask, request

app = Flask(__name__)


def get_model():
    return sum


@app.route("/")
def home():
    f1 = request.args.get('f1')
    f2 = request.args.get('f2')
    f3 = request.args.get('f3')
    f1, f2, f3 = int(f1), int(f2), int(f3)
    model = get_model()
    result = model([f1, f2, f3])
    return str(result)

if __name__ == "__main__":
    app.run()