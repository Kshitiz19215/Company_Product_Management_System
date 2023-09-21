from hashlib import md5
import time as module_time
from config import key

def generate_token(timestamp):
    token_str = key + str(timestamp)
    token = md5(token_str.encode()).hexdigest()
    return token
    

def isValidToken(req_Token, reqTimestamp):
    myToken = generate_token(reqTimestamp)
    if myToken == req_Token:
        return True
    else:
        return False
    
    