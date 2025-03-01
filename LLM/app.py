from flask import Flask, request, render_template, jsonify
import requests
import json
from dotenv import load_dotenv
import os

# Load environment variables from the .env file located in the same directory as app.py
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))

app = Flask(__name__)

# Load configurations from environment variables
LLM_API_URL = os.getenv("LLM_API_URL")
LLM_API_KEY = os.getenv("LLM_API_KEY")

# Function to test LLM vulnerabilities
def test_llm_vulnerabilities(prompt):
    headers = {
        "Authorization": f"Bearer {LLM_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "gpt-4",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }
    response = requests.post(LLM_API_URL, headers=headers, json=payload)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Failed to connect to LLM API. Status Code: {response.status_code}"}

# Flask routes
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        prompt = request.form["prompt"]
        result = test_llm_vulnerabilities(prompt)
        return render_template("home.html", prompt=prompt, result=result)

    return render_template("home.html", prompt=None, result=None)

@app.route("/api/test", methods=["POST"])
def api_test():
    data = request.json
    prompt = data.get("prompt", "")
    result = test_llm_vulnerabilities(prompt)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
