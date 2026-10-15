def greet(name: str | None) -> str:
    """
    Returns a greeting message for the given name.

    If the name is empty or None, it defaults to "World".
    """
    if not name:
        name = "World"
    return f"Hello {name}!"
