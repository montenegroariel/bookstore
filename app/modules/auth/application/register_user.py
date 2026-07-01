from pydantic import BaseModel, EmailStr
from modules.auth.domain.user import User
from modules.auth.ports.repository import UserRepository
from modules.auth.ports.crypto import CryptoService

class RegisterUserDTO(BaseModel):
    email: EmailStr
    password: str

class RegisterUserUseCase:
    def __init__(self, repository: UserRepository, crypto: CryptoService):
        self.repository = repository
        self.crypto = crypto

    async def execute(self, dto: RegisterUserDTO) -> User:
        existing = await self.repository.get_by_email(dto.email)
        if existing:
            raise ValueError("El email ya está registrado")
        
        hashed = self.crypto.hash_password(dto.password)
        new_user = User(id=None, email=dto.email, hashed_password=hashed)
        
        return await self.repository.save(new_user)