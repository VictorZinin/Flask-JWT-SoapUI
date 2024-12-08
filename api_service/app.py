from flask import Flask, request, jsonify
import re
from markupsafe import escape
import jwt

app = Flask(__name__)
SECRET_KEY = 'my_super_secret_key'  

# Handles bearer token authorization
@app.route('/protected', methods=["GET"])
def protected_get():
    auth_header = request.headers.get('Authorization', None)
    if auth_header:
        token = auth_header.split(' ')[1]
        try:
            decoded = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            return jsonify({"status": "success", "data": decoded}), 200
        except jwt.ExpiredSignatureError:
            return jsonify({"status": "error", "message": "Token expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"status": "error", "message": "Invalid token"}), 401
    return jsonify({"status": "error", "message": "Authorization token is missing"}), 401

# Handles the SQL injection
@app.route("/protected", methods=["POST"])
def protected_post():
    data = request.json

    # If nothing was provided as input
    if data is None or "input" not in data or data["input"] == "":
        return jsonify({
            "status": "error", 
            "message": "No input provided or input is empty!"
        }), 400

    user_input = data["input"]
    
    # If it caught SQL Injection
    if re.search(r'[;\'"]', user_input):
        return jsonify({
            "status": "error", 
            "message": "Invalid characters; looks funky!",
            "user_input": user_input
            }), 400
    
    # If no SQL Injection
    return jsonify({
        "status": "success", 
        "user_input": user_input}), 200

if __name__ == '__main__':
    app.run(debug=True)
