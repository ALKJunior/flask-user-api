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
  }
  print(datetime.now(timezone.utc) + timedelta(hours=1))
  return jwt.encode(payload, JWT_SECRET, algorithm="HS256")

def validate_jwt(auth_header):
  header = auth_header.replace("Bearer ", "")
  try:
    token = jwt.decode(header, JWT_SECRET, algorithms="HS256")
    print("token decoded")
    return True, token
  except Exception as e:
    print("token not decoded", e)
    return False, "false"
