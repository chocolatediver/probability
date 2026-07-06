import pandas as pd
from ml.train import train_classifier
from prediction_engine.ml_probability import predict_with_model

def walk_forward_backtest(df: pd.DataFrame, train_window: int = 200, test_window: int = 20, model_type: str = 'random_forest') -> dict:
    data = df.dropna().reset_index(drop=True)
    if len(data) < train_window + test_window + 5:
        raise ValueError('데이터가 부족합니다. limit을 더 크게 설정하세요.')
    returns, predictions = [], []
    start = train_window
    while start + test_window < len(data):
        train_df = data.iloc[start-train_window:start].copy()
        test_df = data.iloc[start:start+test_window].copy()
        model, _ = train_classifier(train_df, model_type=model_type, out_dir='models/walk_forward')
        for idx in range(len(test_df)-1):
            hist = pd.concat([train_df, test_df.iloc[:idx+1]], ignore_index=True)
            prob = predict_with_model(hist, model)
            signal = 1 if prob['p_up'] > 0.55 else 0
            next_return = float(test_df.iloc[idx+1]['return_1']) if pd.notna(test_df.iloc[idx+1]['return_1']) else 0.0
            returns.append(signal * next_return)
            predictions.append(prob['p_up'])
        start += test_window
    r = pd.Series(returns) if returns else pd.Series([0.0])
    equity = (1 + r).cumprod()
    return {'strategy': f'walk_forward_{model_type}', 'total_return': round(float(equity.iloc[-1]-1), 6), 'max_drawdown': round(float((equity/equity.cummax()-1).min()), 6), 'win_rate': round(float((r>0).mean()), 6), 'trades': int((pd.Series(predictions)>0.55).sum()) if predictions else 0, 'windows': len(predictions)}
