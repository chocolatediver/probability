import pandas as pd

def ma_cross_backtest(df: pd.DataFrame, fast: str = "ma_5", slow: str = "ma_20", fee: float = 0.001) -> dict:
    data = df.dropna().copy()
    data["signal"] = (data[fast] > data[slow]).astype(int)
    data["position"] = data["signal"].shift(1).fillna(0)
    data["strategy_return"] = data["position"] * data["return_1"].fillna(0)
    trades = data["position"].diff().abs().fillna(0)
    data["strategy_return"] -= trades * fee
    equity = (1 + data["strategy_return"]).cumprod()
    total_return = float(equity.iloc[-1] - 1) if len(equity) else 0.0
    max_dd = float((equity / equity.cummax() - 1).min()) if len(equity) else 0.0
    win_rate = float((data["strategy_return"] > 0).mean()) if len(data) else 0.0
    return {
        "strategy": "ma_cross",
        "total_return": round(total_return, 6),
        "max_drawdown": round(max_dd, 6),
        "win_rate": round(win_rate, 6),
        "trades": int(trades.sum()),
    }
