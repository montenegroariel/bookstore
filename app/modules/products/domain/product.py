from dataclasses import dataclass

@dataclass
class Product:
    id: str | None
    name: str
    price: float

# modules/products/ports/repository.py
from abc import ABC, abstractmethod
from modules.products.domain.product import Product

class ProductRepository(ABC):
    @abstractmethod
    async def create(self, product: Product) -> Product:
        pass

    @abstractmethod
    async def list_all(self) -> list[Product]:
        pass