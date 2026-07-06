from pathlib import Path
import datetime

ROOT = Path(__file__).resolve().parents[1]
TODAY = datetime.date.today().isoformat()

def append_changelog(message: str):
    path = ROOT / "docs" / "CHANGELOG.md"
    with path.open("a", encoding="utf-8") as f:
        f.write(f"\n## Update - {TODAY}\n- {message}\n")

def update_progress(message: str):
    path = ROOT / "docs" / "PROGRESS.md"
    with path.open("a", encoding="utf-8") as f:
        f.write(f"\n## Update - {TODAY}\n- {message}\n")

if __name__ == "__main__":
    msg = "Manual progress update hook executed."
    append_changelog(msg)
    update_progress(msg)
    print("Docs updated.")
