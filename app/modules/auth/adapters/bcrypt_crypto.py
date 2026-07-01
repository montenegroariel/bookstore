from modules.auth.ports.crypto import CryptoService

class FakeCryptoService(CryptoService):
    def hash_password(self, password: str) -> str:
        return f"hashed_{password}"  # Reemplazar con bcrypt/passlib en producción

    def verify_password(self, password: str, hashed: str) -> bool:
        return f"hashed_{password}" == hashed