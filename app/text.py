def slugify(s: str) -> str:
    return "-".join("".join(c.lower() if c.isalnum() else " " for c in s).split())
