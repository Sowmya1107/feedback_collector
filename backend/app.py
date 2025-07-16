from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from datetime import datetime
from feedback_store import feedback_store
import os

# Initialize app
app = Flask(__name__, static_folder='../frontend', static_url_path='/')
CORS(app)

@app.route('/')
def serve_html():
    return send_from_directory('../frontend', 'index.html')

@app.route('/feedback', methods=['POST'])
def submit_feedback():
    data = request.get_json()
    print("Received data:", data)

    feedback = {
        "text": data.get("text", "")[:250],
        "rating": int(data.get("rating", 0)),
        "timestamp": datetime.now().isoformat()
    }

    feedback_store.append(feedback)
    return jsonify({"message": "Feedback added"}), 201

@app.route('/feedback', methods=['GET'])
def get_feedback():
    return jsonify(feedback_store), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
