from core.config_loader import ConfigLoader

def test_config_loader_app():
    cfg = ConfigLoader().load("app")
    assert "app" in cfg
    assert cfg["app"]["name"] == "Probability Platform"

def test_config_loader_all():
    cfg = ConfigLoader().load_all()
    assert "app" in cfg
    assert "crypto" in cfg
