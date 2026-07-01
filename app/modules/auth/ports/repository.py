from abc import ABC, abstractmethod
from modules.auth.domain.user import User

class UserRepository(ABC):
    @abstractmethod
    async def save(self, user: User) -> User:
        pass

    @abstractmethod
    async def get_by_email(self, email: str) -> User | None:
        pass