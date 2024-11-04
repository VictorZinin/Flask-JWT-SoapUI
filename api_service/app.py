from flask import Flask, request, jsonify
import jwt

app = Flask(__name__)
SECRET_KEY = 'my_super_secret_key'  

@app.route('/protected')
def protected():
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

if __name__ == '__main__':
    app.run(debug=True)
