from pydantic import BaseModel, Field

class DemandRequest(BaseModel):
    sku_id: int = Field(..., description="SKU identifier")
    price: float
    promo_flag: int
    season: int

class ChurnRequest(BaseModel):
    customer_id: int
    recency: int
    frequency: int
    monetary: float

class SegmentRequest(BaseModel):
    recency: int
    frequency: int
    monetary: float

class InventoryRequest(BaseModel):
    sku_id: int
    stock: int
    demand: int
    lead_time: int