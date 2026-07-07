# Probability Platform

AI 기반 멀티마켓 확률 예측 플랫폼입니다.

## Version
v0.6.0

## v0.6.0 핵심 변경
- `pyproject.toml` 기반 프로젝트 표준화
- `ruff`, `black`, `mypy`, `pytest` 설정
- Config YAML 시스템
- Logging setup
- Collector Factory
- Model Registry
- GitHub Actions 개선

## 설치
```bash
pip install -e ".[dev]"
```

## Dashboard
```bash
streamlit run dashboard/streamlit_app.py
```

## 모델 목록
```bash
python scripts/list_models.py
```

## 테스트
```bash
pytest -q
```
