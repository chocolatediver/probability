# Model Card

## v0.4 ML Classifier

### 목적
다음 캔들의 상승/하락 확률을 분류한다.

### 입력
- 수익률
- 이동평균
- EMA
- RSI
- MACD
- ATR
- Bollinger
- Stochastic
- OBV
- VWAP

### 출력
- P(UP)
- P(DOWN)
- Confidence
- Accuracy / Precision / Recall / ROC-AUC

### 제한
- 현재는 연구용 기본 모델
- 실거래 판단에는 Walk-forward 검증 필요
