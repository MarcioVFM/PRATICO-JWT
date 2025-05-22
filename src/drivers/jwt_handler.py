import jwt
from datetime import datetime, timedelta, timezone

class JwtHandler:
    def create_token_jwt(self, body: dict) -> str:
        token = jwt.encode(
            payload={
                    'exp': datetime.now(timezone.utc) + timedelta(hours=10),
                    **body
            },
            key='segredo',
            algorithm='HS256'
        )
        return token
    
    def decode_jwt_token(self, token: str) -> dict:
        token_information = jwt.decode(token, key='segredo', algorithms='HS256')
        return token_information
