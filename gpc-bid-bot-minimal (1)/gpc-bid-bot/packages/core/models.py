from __future__ import annotations
from pydantic import BaseModel, Field
from typing import Optional, Literal, List
from datetime import datetime

class RFQ(BaseModel):
    id: str
    source: Literal["state_local","federal","other"]
    url: Optional[str] = None
    title: str
    raw_text: str
    qty: int
    due_ts: Optional[datetime] = None
    ship_zip: Optional[str] = None
    budget_cents: Optional[int] = None
    payment_hints: List[str] = Field(default_factory=list)
    blacklist_hits: List[str] = Field(default_factory=list)

class SupplierOffer(BaseModel):
    supplier: Literal["zoro","global_industrial","other"]
    unit_price_cents: int
    in_stock: bool
    ship_days: int
    ship_cost_cents: int

class ScoredOpportunity(BaseModel):
    rfq_id: str
    supplier: str
    landed_cents: int
    card_fee_cents: int
    offer_price_cents: int
    margin_bps: int
    pass_reasons: List[str] = Field(default_factory=list)
    drop_reasons: List[str] = Field(default_factory=list)
    passed: bool

class QuoteSpec(BaseModel):
    rfq_id: str
    supplier: str
    offer_price_cents: int
    qty: int
    ship_days: int
    ship_cost_cents: int
    due_ts: Optional[datetime] = None
    ship_zip: Optional[str] = None
