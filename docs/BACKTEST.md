# Backtest

## v0.5 지원 백테스트

### 1. MA Cross Backtest
단순 이동평균 교차 전략입니다.

### 2. Walk-forward ML Backtest
일정 구간을 학습하고 다음 구간을 검증하여 미래 데이터 누수를 줄입니다.

## 실행
```bash
python scripts/run_walk_forward.py --market crypto --symbol BTC/USDT --limit 800
```
