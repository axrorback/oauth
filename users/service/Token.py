from uuid import uuid4

class TokenService:
    @staticmethod
    def registration_token():
        return str(uuid4())

    @staticmethod
    def reset_token():
        return str(uuid4())
    @staticmethod
    def hash(token: str) -> str:
        return hashlib.sha256(token.encode()).hexdigest()