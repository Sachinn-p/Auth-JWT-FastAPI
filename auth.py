from jose import JWTError, jwt
from datetime import datetime, timedelta

SECRET_KEY = "!@#$%^&*()0987654321"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTE = 15
REFRESH_TOKEN_EXPIRE_MINUTE = 15 * 60

def create_token(data :dict, expire_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expire_delta
    to_encode.update({"exp" : expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
    
