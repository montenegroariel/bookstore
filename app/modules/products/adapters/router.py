from fastapi import APIRouter, Depends
from modules.products.application.create_product import CreateProductUseCase, CreateProductDTO
from modules.products.ports.repository import ProductRepository
from modules.products.domain.product import Product


# Simulación de adaptador de persistencia para productos
class InMemoryProductRepository(ProductRepository):
    def __init__(self):
        self._products = []
        self._id_gen = 1
        
    async def create(self, product: Product) -> Product:
        product.id = str(self._id_gen)
        self._products.append(product)
        self._id_gen += 1
        return product
        
    async def list_all(self) -> list[Product]:
        return self._products

router = APIRouter(prefix="/products", tags=["Products"])
product_repo = InMemoryProductRepository()

def get_create_product_use_case() -> CreateProductUseCase:
    return CreateProductUseCase(repository=product_repo)

@router.post("/", status_code=201)
async def create_product(dto: CreateProductDTO, use_case: CreateProductUseCase = Depends(get_create_product_use_case)):
    product = await use_case.execute(dto)
    return product