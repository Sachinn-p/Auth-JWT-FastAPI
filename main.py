from fastapi import FastAPI, HTTPException, Depends, Header
from datetime import timedelta
from auth import create_token, verify_token
from models import get_user, verify_password
from schemas import LoginRequest, TokenResponse

app = FastAPI()

@app.post("/login", response_model=TokenResponse)
def login(request: LoginRequest):
    user = get_user(request.username)
    if not user or not verify_password(request.password, user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Invalid credientials")
    access = create_token({"sub" : request.username}, timedelta(minutes=15))
    refresh = create_token({"sub" : request.username}, timedelta(minutes=1440))
    return {"access_token" : access, "refresh_token" : refresh, "token_type": "bearer"}

@app.get("/profile")
def profile(authorization : str = Header(...)):
    token = authorization.replace("Bearer ", "")
    payload = verify_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return {"message" : f"Welcome, {payload['sub']}!"}