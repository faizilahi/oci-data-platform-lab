from pathlib import Path

def list_parts(prefix: Path) -> list:
    return sorted(prefix.glob("part-*.csv"))

def has_success(prefix: Path) -> bool:
    return (prefix / "_SUCCESS").exists()
