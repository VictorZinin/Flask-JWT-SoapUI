import jwt
import datetime

def generate_jwt(user_id='user123', username='John Doe', minutes_valid=60, minutes_before_now=0, incorrect_signature=False):
    # for demonstration purposes 
    secret = 'incorrect_secret' if incorrect_signature else 'my_super_secret_key'
    algorithms = 'HS256'

    payload = {
        'sub': user_id,
        'name': username,
        'admin': False,
        'iat': datetime.datetime.utcnow() - datetime.timedelta(minutes=minutes_before_now),
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=minutes_valid)
    }

    try:
        token = jwt.encode(payload, secret, algorithm=algorithms)
    except Exception as e:
        print(f"Error encoding JWT: {e}")
        return None
    
    return token

def save_tokens_to_file():
    valid_token = generate_jwt()
    expired_token = generate_jwt(minutes_valid=-5)  # Already expired
    incorrect_signature_token = generate_jwt(incorrect_signature=True)

    with open('jwt_tokens.txt', 'w') as file:
        file.write("Valid JWT Token:\n" + str(valid_token) + "\n\n")
        file.write("Expired JWT Token:\n" + str(expired_token) + "\n\n")
        file.write("Incorrect Signature JWT Token:\n" + str(incorrect_signature_token) + "\n")

if __name__ == "__main__":
    save_tokens_to_file()
