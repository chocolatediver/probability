# Architecture

## v0.6.0 Architecture

```text
Config Layer
  ├── YAML Config
  ├── Runtime Config
  └── Logging

Collector Layer
  ├── CollectorFactory
  ├── CryptoCollector
  ├── USStockCollector
  └── KoreaStockCollector

Data Layer
  ├── Normalizer
  ├── SQLite
  ├── Parquet
  └── DuckDB

AI Layer
  ├── ModelRegistry
  ├── RandomForest
  ├── GradientBoosting
  ├── XGBoost optional
  ├── LightGBM optional
  └── CatBoost optional
```
