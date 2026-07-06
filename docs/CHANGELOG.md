# Changelog

## v0.1.0 - 2026-07-01
### Added
- 초기 프로젝트 구조
- 시장 선택 CLI
- Crypto/US/Korea Collector Stub
- Data Normalizer
- Basic Feature Engine
- Probability Engine Stub
- 문서 관리 체계

## v0.2.0 - 2026-07-03
### Added
- SQLite 저장소
- RSI/MACD/ATR 기술지표
- CSV 예측 리포트
- Dashboard Preview CLI
- 저장/리포트 옵션: `--save`, `--report`

## v0.3.0 - 2026-07-03
### Added
- CCXT 기반 Crypto Collector 구조
- yfinance 기반 US Stock Collector 구조
- KIS 한국시장 Collector 준비 구조
- Parquet/CSV 컬럼 저장소
- Bollinger/Stochastic/OBV/VWAP 지표
- MA Cross 백테스트
- Streamlit 대시보드 초안

## v0.4.0 - 2026-07-03
### Added
- ML 학습 파이프라인
- RandomForest / GradientBoosting Classifier
- 학습 메트릭 JSON 저장
- Markdown 연구 리포트
- `train_model.py`
- Streamlit ML 학습 옵션

## v0.5.0 - 2026-07-06
### Added
- Binance WebSocket realtime collector
- Upbit WebSocket realtime collector
- DuckDB storage layer
- Realtime event persistence
- Walk-forward ML backtest
- GitHub Actions CI
- AGENTS.md and CLAUDE.md
- Realtime stream CLI
- Walk-forward CLI

### Changed
- README updated for GitHub-based workflow
- Main CLI supports `--walk-forward` and `--duckdb`

## v0.5.1 - 2026-07-06
### Added
- `probability_version.py`
- `config/runtime.py`
- `scripts/query_duckdb.py`
- `scripts/project_status.py`
- Stream runner `--max-events` support
