# app/modules/sales/domain/entities.py
from dataclasses import dataclass
from decimal import Decimal
from datetime import datetime
from typing import List, Optional

@dataclass
class SaleItemDomain:
    product_id: int
    quantity: int
    price_at_sale: Optional[Decimal] = None
    cost_at_sale: Optional[Decimal] = None

@dataclass
class SaleDomain:
    payment_method: str
    items: List[SaleItemDomain]
    customer_id: Optional[int] = None
    id: Optional[int] = None
    total_amount: Optional[Decimal] = None
    sale_date: Optional[datetime] = None