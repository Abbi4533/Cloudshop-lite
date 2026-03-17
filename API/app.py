from flask import Flask, jsonify
import redis
import os

app = Flask(__name__)

redis_host = os.getenv("REDIS_HOST", "localhost")
r = redis.Redis(host=redis_host, port=6379, decode_responses=True)

@app.route("/")
def home():
    return jsonify({"message": "API running"})

@app.route("/count")
def count():
    value = r.incr("counter")
    return jsonify({"visits": value})

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)