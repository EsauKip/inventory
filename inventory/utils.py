import jwt
from datetime import datetime, timedelta

def get_access_token(payload,days):
    token =jwt.encode(
        {"exp":datetime.now() + timedelta(days=days),**payload},
        settings.SECRET_KEY
    )