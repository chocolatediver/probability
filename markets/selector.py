from collectors.factory import CollectorFactory

def get_collector(market: str):
    return CollectorFactory.create(market)
