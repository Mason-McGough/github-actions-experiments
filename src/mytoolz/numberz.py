from typing import Any


def is_number(x: Any) -> bool:
    """
    Check if x is a number.

    Args:
        x: Object to check.

    Returns:
        True if x is a number, False otherwise.

    """
    return isinstance(x, (int, float, complex))
