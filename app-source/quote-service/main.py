from flask import Flask, jsonify
import random

app = Flask(__name__)

QUOTES = [
    {"quote": "The best way to predict the future is to invent it.", "author": "Alan Kay"},
    {"quote": "Simplicity is the soul of efficiency.", "author": "Austin Freeman"},
    {"quote": "Make it work, make it right, make it fast.", "author": "Kent Beck"},
    {"quote": "Infrastructure as code is the foundation of modern platforms.", "author": "Unknown"},
    {"quote": "You build it, you run it.", "author": "Werner Vogels"},
]

@app.route("/quote")
def get_quote():
    return jsonify(random.choice(QUOTES))

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
