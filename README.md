# 🔐 JWT Login API with FastAPI

A simple FastAPI-based authentication system using JSON Web Tokens (JWT) for secure login and route protection.

## 🚀 Features

- ✅ JWT-based Authentication (Access + Refresh Tokens)
- ✅ Secure login endpoint
- ✅ Protected route with Bearer token
- ✅ Password hashing with bcrypt
- 🧪 Ready for testing with Postman or curl

---

## 🧱 Tech Stack

- **Backend**: FastAPI
- **JWT Handling**: python-jose
- **Password Hashing**: passlib[bcrypt]
- **Environment**: Python 3.10+

---

## 📦 Installation

```bash
git clone https://github.com/your-username/auth-jwt-fastapi.git
cd auth-jwt-fastapi
pip install -r requirements.txt
uvicorn main:app --reload
