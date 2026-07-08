from ml.model_factory import create_classifier

def test_create_baseline_models():
    assert create_classifier("random_forest") is not None
    assert create_classifier("gradient_boosting") is not None
