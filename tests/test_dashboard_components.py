from dashboard.components.status_card import signal_from_probability
from dashboard.components.market_selector import DEFAULT_SYMBOLS

def test_signal_from_probability():
    assert signal_from_probability(0.7) == "BUY"
    assert signal_from_probability(0.3) == "SELL"
    assert signal_from_probability(0.5) == "HOLD"

def test_market_symbols():
    assert "crypto" in DEFAULT_SYMBOLS
    assert "us" in DEFAULT_SYMBOLS
    assert "korea" in DEFAULT_SYMBOLS
