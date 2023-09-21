from config import key
from hashlib import md5
import time

def generate_token():
    timestamp = str(time.time())
    token_str = key + timestamp
    token = md5(token_str.encode()).hexdigest()
    return token

token = generate_token()
timestamp = str(time.time())

print("Token:", token)
print("Timestamp:", timestamp)
print(key)
