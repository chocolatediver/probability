from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main():
    docs = ["PROGRESS.md", "CHANGELOG.md", "TODO.md", "ROADMAP.md"]
    print("Project status documents:")
    for doc in docs:
        path = ROOT / "docs" / doc
        print(f"- {doc}: {'OK' if path.exists() else 'MISSING'}")

if __name__ == "__main__":
    main()
