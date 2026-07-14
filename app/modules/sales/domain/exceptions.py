# app/modules/sales/domain/exceptions.py
class InsufficientStockException(Exception):
    def __init__(self, product_name: str, available: int):
        self.message = f"Stock insuficiente para '{product_name}'. Disponible: {available}"
        super().__init__(self.message)

class ProductNotFoundException(Exception):
    def __init__(self, product_id: int):
        self.message = f"El producto con ID {product_id} no existe."
        super().__init__(self.message)