from ml.registry import ModelRegistry

def test_model_registry_baselines():
    names = ModelRegistry().available_names()
    assert "random_forest" in names
    assert "gradient_boosting" in names
