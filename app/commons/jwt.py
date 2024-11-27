from datetime import datetime, timedelta, timezone
import jwt
import os

JWT_SECRET = os.getenv('JWT_SECRET')

def create_jwt_token(user):
  user_data = user.to_json()
  payload = {
    "sub": str(user_data["id"]),
    "exp": datetime.now(timezone.utc) + timedelta(hours=1),
    "iat": datetime.now(timezone.utc),
    "username": user_data["username"],
    "email": user_data["email"],
    "status": user_data["status"],
    "createdAt": user_data["createdAt"],
    "role": user_data["role"],
  }
  print(datetime.now(timezone.utc) + timedelta(hours=1))
  return jwt.encode(payload, JWT_SECRET, algorithm="HS256")

def validate_jwt(auth_header):
  header = auth_header.replace("Bearer ", "")
  try:
    user_data = jwt.decode(header, JWT_SECRET, algorithms="HS256")
    return True, user_data
  except Exception as e:
    print("token not decoded", e)
    return False, "false"
