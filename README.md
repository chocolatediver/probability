# Probability Platform

AI 기반 멀티마켓 확률 예측 플랫폼입니다.

## Version
v0.6.2

## v0.6.2 핵심 변경
- SHAP 기반 Explainability 구조
- Feature Importance fallback
- Optuna 하이퍼파라미터 탐색 구조
- Leaderboard DuckDB 저장
- Feature Importance DuckDB 저장
- Dashboard Explainability 패널

## 설치
```bash
pip install -e ".[dev]"
```

선택 ML/Explainability까지 설치:
```bash
pip install -e ".[dev,ml]"
```

## Explainability
```bash
python scripts/run_explainability.py --market crypto --symbol BTC/USDT --model random_forest --save
```

## Optuna
```bash
python scripts/run_optuna.py --market crypto --symbol BTC/USDT --model random_forest --trials 20
```

## Dashboard
```bash
streamlit run dashboard/streamlit_app.py
```
