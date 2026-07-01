from abc import ABC, abstractmethod
from modules.products.domain.product import Product

class ProductRepository(ABC):  # <- Revisa que se llame exactamente así
    @abstractmethod
    async def create(self, product: Product) -> Product:
        ...

    @abstractmethod
    async def list_all(self) -> list[Product]:
        pass