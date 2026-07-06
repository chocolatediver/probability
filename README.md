# AI Multi-Market Quant Platform

Crypto, US Stock, Korea Stock 시장을 선택적으로 수집·정규화·분석하기 위한 Python 기반 AI 퀀트 플랫폼 골격입니다.

## 현재 버전
v0.1.0

## 실행
```bash
python -m scripts.init_project_status
python main.py --market crypto --symbol BTC/USDT
python main.py --market us --symbol AAPL
python main.py --market korea --symbol 005930
```

## 핵심 구조
- `collectors/`: 시장별 데이터 수집기
- `normalize/`: 공통 OHLCV 스키마 변환
- `feature_engine/`: 기술지표 생성
- `prediction_engine/`: 확률 예측 엔진
- `docs/PROGRESS.md`: 진행률 관리
- `docs/CHANGELOG.md`: 변경 이력
- `docs/TODO.md`: 작업 목록
