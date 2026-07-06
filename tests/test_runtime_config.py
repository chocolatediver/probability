from config.runtime import get_runtime_config

def test_runtime_config():
    cfg = get_runtime_config()
    assert cfg.data_dir.exists()
    assert cfg.stream_max_events >= 1
