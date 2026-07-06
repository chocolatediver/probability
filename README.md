# Probability Platform

AI 기반 멀티마켓 확률 예측 플랫폼입니다.

## Version
v0.5.1

## v0.5.1 핵심 변경
- 실시간 수집 안전 종료 옵션 `--max-events`
- DuckDB 조회 CLI
- 프로젝트 상태 점검 CLI
- Runtime config
- Version module

## 설치
```bash
pip install -r requirements.txt
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

## 프로젝트 상태
```bash
python scripts/project_status.py
```
