from collectors.factory import CollectorFactory

def test_collector_factory_crypto():
    assert CollectorFactory.create("crypto") is not None

def test_collector_factory_us():
    assert CollectorFactory.create("us") is not None

def test_collector_factory_korea():
    assert CollectorFactory.create("korea") is not None
