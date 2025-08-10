from packages.rules.loader import load_rules

def test_rules_load():
    r = load_rules()
    assert r.thresholds["max_ship_days"] == 10
    assert "RFQ" in r.include
