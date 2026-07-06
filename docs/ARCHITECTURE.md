# Architecture

```text
Market Selector
   ├── Crypto Collector
   ├── US Stock Collector
   └── Korea Stock Collector
        ↓
Data Normalizer
        ↓
Feature Engine
        ↓
Prediction Engine
        ↓
Dashboard / Report / Backtest
```

## 공통 데이터 스키마
| field | description |
|---|---|
| datetime | UTC/KST 변환 가능한 시간 |
| market | crypto/us/korea |
| symbol | 종목 코드 |
| open/high/low/close | 가격 |
| volume | 거래량 |
| source | 데이터 출처 |
