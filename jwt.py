from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "super-secret-key"
ALGORITHM = "HS256"


data = {"sub": "emailr@email.com"}


expire = datetime.utcnow() + timedelta(hours=3)
data.update({"exp": expire})


token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
print("JWT token:", token)


decoded = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
print("Decoded:", decoded)