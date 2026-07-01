from pydantic import BaseModel, Field
from modules.products.domain.product import Product
from modules.products.ports.repository import ProductRepository

class CreateProductDTO(BaseModel):
    name: str = Field(..., min_length=3)
    price: float = Field(..., gt=0)

class CreateProductUseCase:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    async def execute(self, dto: CreateProductDTO) -> Product:
        product = Product(id=None, name=dto.name, price=dto.price)
        return await self.repository.create(product)