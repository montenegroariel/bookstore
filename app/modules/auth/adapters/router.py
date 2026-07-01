from fastapi import APIRouter, Depends, HTTPException, status
from modules.auth.application.register_user import RegisterUserUseCase, RegisterUserDTO
from modules.auth.adapters.sql_repository import InMemoryUserRepository
from modules.auth.adapters.bcrypt_crypto import FakeCryptoService

router = APIRouter(prefix="/auth", tags=["Auth"])

# Instancias compartidas (en una app real usarías un contenedor de DI como 'punq' o 'dishka')
user_repo = InMemoryUserRepository()
crypto_service = FakeCryptoService()

def get_register_use_case() -> RegisterUserUseCase:
    return RegisterUserUseCase(repository=user_repo, crypto=crypto_service)

@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(dto: RegisterUserDTO, use_case: RegisterUserUseCase = Depends(get_register_use_case)):
    try:
        user = await use_case.execute(dto)
        return {"id": user.id, "email": user.email}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))