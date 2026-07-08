from pathlib import Path
from probability_version import VERSION, APP_NAME

DOCS = ["docs/PROGRESS.md", "docs/CHANGELOG.md", "docs/TODO.md", "docs/BACKTEST.md", "docs/MODEL_CARD.md", "docs/ARCHITECTURE.md"]

def main():
    root = Path(__file__).resolve().parents[1]
    print(f"{APP_NAME} v{VERSION}")
    print("=" * 40)
    for doc in DOCS:
        path = root / doc
        print(f"{doc}: {'OK' if path.exists() else 'MISSING'}")
    print("=" * 40)
    print("Current sprint: Development Infrastructure")
    print("Next: v0.6.1 AI model extension")

if __name__ == "__main__":
    main()
