from modules.auth.ports.repository import UserRepository
from modules.auth.domain.user import User

class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self._db = {}
        self._counter = 1

    async def save(self, user: User) -> User:
        user.id = str(self._counter)
        self._db[user.id] = user
        self._counter += 1
        return user

    async def get_by_email(self, email: str) -> User | None:
        return next((u for u in self._db.values() if u.email == email), None)