import asyncio, json, time
from typing import Callable, Dict, Any
from .base_stream import BaseStreamCollector

class UpbitStreamCollector(BaseStreamCollector):
    def _upbit_symbol(self) -> str:
        if '-' in self.symbol: return self.symbol
        parts = self.symbol.split('/')
        return f"{parts[1]}-{parts[0]}" if len(parts)==2 else self.symbol

    async def stream_trades(self, on_message: Callable[[Dict[str, Any]], None]):
        try:
            import websockets
            url = 'wss://api.upbit.com/websocket/v1'
            payload = [{'ticket':'probability'}, {'type':'trade', 'codes':[self._upbit_symbol()]}]
            async with websockets.connect(url, ping_interval=20) as ws:
                await ws.send(json.dumps(payload))
                async for raw in ws:
                    msg = json.loads(raw.decode('utf-8') if isinstance(raw, bytes) else raw)
                    on_message({'market':'crypto','exchange':'upbit','type':'trade','symbol':self.symbol,'timestamp':msg.get('trade_timestamp'),'price':float(msg.get('trade_price')),'quantity':float(msg.get('trade_volume')),'side':msg.get('ask_bid','').lower(),'raw':msg})
        except Exception:
            for i in range(5):
                on_message({'market':'crypto','exchange':'upbit_sample','type':'trade','symbol':self.symbol,'timestamp':int(time.time()*1000),'price':100000000+i*1000,'quantity':0.001,'side':'bid','raw':{}})
                await asyncio.sleep(0.1)

    async def stream_orderbook(self, on_message: Callable[[Dict[str, Any]], None]):
        on_message({'market':'crypto','exchange':'upbit_sample','type':'orderbook','symbol':self.symbol,'timestamp':int(time.time()*1000),'bids':[[100000000,1.0]],'asks':[[100001000,0.8]],'raw':{}})
