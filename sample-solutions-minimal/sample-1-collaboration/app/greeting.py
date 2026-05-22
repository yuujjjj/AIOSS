def get_greeting(name: str) -> str:
    """이름을 받아 인사말을 반환하세요."""
    if not name:
        return "Hello, Guest!"
    return f"Hello, {name}!"
