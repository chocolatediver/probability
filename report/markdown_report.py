from pathlib import Path
import datetime

def export_markdown_report(prediction: dict, backtest: dict | None = None, metrics: dict | None = None, out_dir: str = "data/processed"):
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    now = datetime.datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    path = Path(out_dir) / f"quant_report_{now}.md"

    lines = [
        "# AI Multi-Market Quant Report",
        "",
        f"Generated UTC: {now}",
        "",
        "## Prediction",
        f"- P(UP): {prediction.get('p_up')}",
        f"- P(DOWN): {prediction.get('p_down')}",
        f"- Confidence: {prediction.get('confidence')}",
        f"- Model: {prediction.get('model')}",
        "",
    ]

    if backtest:
        lines += [
            "## Backtest",
            f"- Strategy: {backtest.get('strategy')}",
            f"- Total Return: {backtest.get('total_return')}",
            f"- Max Drawdown: {backtest.get('max_drawdown')}",
            f"- Win Rate: {backtest.get('win_rate')}",
            f"- Trades: {backtest.get('trades')}",
            "",
        ]

    if metrics:
        lines += [
            "## ML Metrics",
            f"- Model Type: {metrics.get('model_type')}",
            f"- Accuracy: {metrics.get('accuracy')}",
            f"- Precision: {metrics.get('precision')}",
            f"- Recall: {metrics.get('recall')}",
            f"- ROC-AUC: {metrics.get('roc_auc')}",
            "",
        ]

    path.write_text("\n".join(lines), encoding="utf-8")
    return path
