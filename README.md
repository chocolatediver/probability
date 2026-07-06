# Probability Platform

AI 기반 멀티마켓 확률 예측 플랫폼입니다.

## Version
v0.5.2

## v0.5.2 핵심 변경
- Dashboard Framework
- Market Selector
- Status Card
- Chart Panel
- DuckDB Explorer
- OrderBook Panel
- Log Panel

## 설치
```bash
pip install -r requirements.txt
```

## 기본 실행
```bash
python main.py --market crypto --symbol BTC/USDT --parquet --backtest --train --report
```

## 실시간 스트림
```bash
python scripts/run_realtime_stream.py --exchange binance --symbol BTC/USDT --type trade --max-events 20
python scripts/run_realtime_stream.py --exchange upbit --symbol BTC/KRW --type orderbook --max-events 20
```

## DuckDB 조회
```bash
python scripts/query_duckdb.py --name events
python scripts/query_duckdb.py --name trades
python scripts/query_duckdb.py --name backtests
```

## Dashboard
```bash
streamlit run dashboard/streamlit_app.py
```

## 프로젝트 상태
```bash
python scripts/project_status.py
```
