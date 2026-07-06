# Release Note v0.5.1

Date: 2026-07-06

## Summary
실시간 수집 모듈의 안전성과 GitHub 기반 운영 편의성을 개선한 패치 버전입니다.

## Added
- Version module
- Runtime config module
- DuckDB query CLI
- Project status CLI
- Bounded realtime stream collection

## Run
```bash
python scripts/run_realtime_stream.py --exchange binance --symbol BTC/USDT --type trade --max-events 20
python scripts/query_duckdb.py --name events
python scripts/project_status.py
```
