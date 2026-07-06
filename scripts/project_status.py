from pathlib import Path
from probability_version import VERSION, APP_NAME

DOCS = ["docs/PROGRESS.md", "docs/CHANGELOG.md", "docs/TODO.md", "docs/BACKTEST.md", "docs/MODEL_CARD.md"]

def main():
    root = Path(__file__).resolve().parents[1]
    print(f"{APP_NAME} v{VERSION}")
    print("=" * 40)
    for doc in DOCS:
        print(f"{doc}: {'OK' if (root / doc).exists() else 'MISSING'}")
    print("=" * 40)
    print("Next: v0.5.2 dashboard and model extension")

if __name__ == "__main__":
    main()
