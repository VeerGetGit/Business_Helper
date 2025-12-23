from flask import Flask, request, jsonify
from ai_logic import generate_specifications

app = Flask(__name__)

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json(silent=True)

    if not data or "requirement" not in data:
        return jsonify({"error": "Requirement text is required"}), 400

    result = generate_specifications(data["requirement"])

    # ALWAYS return JSON
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
