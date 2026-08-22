from flask import Flask, jsonify
import os
import time

app = Flask(__name__)
START_TIME = time.time()

@app.route("/")
def home():
    return jsonify({
        "application": "Kubernetes DevOps Demo",
        "status": "running",
        "version": os.getenv("APP_VERSION", "1.0.0"),
        "environment": os.getenv("ENVIRONMENT", "development")
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/ready")
def ready():
    return jsonify({"status": "ready"})

@app.route("/metrics")
def metrics():
    uptime = int(time.time() - START_TIME)
    return f"""# HELP app_uptime_seconds Application uptime
# TYPE app_uptime_seconds gauge
app_uptime_seconds {uptime}
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
