from dataclasses import dataclass

@dataclass # TODO: Repasar concepto de decoradores
class User:
    id: str | None
    email: str
    hashed_password: str