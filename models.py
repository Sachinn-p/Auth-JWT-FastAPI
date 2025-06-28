from typing import Optional
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Precomputed bcrypt hash for "^^yP@$$w0rd"
db = {
    "sachin": {
        "username": "sachin",
        # This hash is for "^^yP@$$w0rd". If you change the password, regenerate the hash.
        # Hash for "^^yP@$w0rd" generated with passlib
        "hashed_password": "$2b$12$vVKq9zf5IIbhYRa/7cvPu.LQnV/seCIgmoXzyN1qG4LAN2MZ6biau",  # Correct hash for ^^yP@$w0rd
        "email": "sachin@example.com"
    }
}

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a plain password against its hash."""
    return pwd_context.verify(plain_password, hashed_password)

def get_user(username: str) -> Optional[dict]:
    """Retrieve a user from the database by username (case-insensitive)."""
    for key, user in db.items():
        if key.lower() == username.lower():
            return user
    return None