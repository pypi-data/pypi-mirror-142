from dataclasses import dataclass
from datetime import datetime


@dataclass
class OrderConfirm:
    accountNumber: str
    quantity: int
    price: int
    ticker: str
    instrumentType: str
    quantityType: str
    operationType: str
    operationTerm: str
    operationMaxDate: datetime
    operation: str
    settlement: str
    disclaimers: str
    externalId: str

