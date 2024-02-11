from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/sports", methods=["POST"])
def sports():
    data = request.json
    name = data["name"]
    member = data["member"]
    return jsonify({"name": name, "member": member})


if __name__ == "__main__":
    app.run(debug=True, port=5001)
