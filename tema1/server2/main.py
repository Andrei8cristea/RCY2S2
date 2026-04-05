#########
# 2
#########
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "nume": "Andrei Cristea",
        "nr_matricol": "208/2024"
    })

#endpoint pt curl
@app.route("/items/<item_id>", methods=["GET"])
def get_item(item_id):
    return jsonify({"item_id": item_id})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001)