from packages.core.models import RFQ, SupplierOffer, ScoredOpportunity, QuoteSpec
from packages.core.contracts import validate_transition, Stage

def test_models_instantiable():
    RFQ(id="1", source="state_local", title="T", raw_text="x", qty=1)
    SupplierOffer(supplier="zoro", unit_price_cents=1000, in_stock=True, ship_days=5, ship_cost_cents=0)
    ScoredOpportunity(rfq_id="1", supplier="zoro", landed_cents=1000, card_fee_cents=30, offer_price_cents=1200, margin_bps=2000, passed=True)
    QuoteSpec(rfq_id="1", supplier="zoro", offer_price_cents=1200, qty=1, ship_days=5, ship_cost_cents=0)

def test_transitions():
    assert validate_transition(Stage.PARSED, Stage.OFFERED)
    assert not validate_transition(Stage.QUOTED, Stage.SCORED)
