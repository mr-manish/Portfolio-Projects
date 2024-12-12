from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from main import main_func

load_dotenv()


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    name = request.form["name"]
    return main_func(name=name)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
