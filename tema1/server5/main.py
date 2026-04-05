from flask import Flask, request, jsonify
import math

app = Flask(__name__)


@app.route("/subnet", methods=["POST"])
def calc_subnet():
    data = request.get_json()
    noduri = data["noduri"]

    #gasesc numarul minim de biti pe care ii folosc la adresele de host
    bits = math.ceil(math.log2(noduri + 2))  # adun 2  pr cele speciale (nefolosibile)

    prefix = 32 - bits

    #il transform in subnet mask
    mask = []
    remaining = prefix
    for _ in range(4):
        if remaining >= 8:
            mask.append(255)
            remaining -= 8
        else:
            val = (256 - 2**(8 - remaining)) if remaining > 0 else 0
            mask.append(val)
            remaining = 0

    subnet_mask = ".".join(map(str, mask))

    return jsonify({
        "cidr": f"/{prefix}",
        "mask": subnet_mask
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001)
