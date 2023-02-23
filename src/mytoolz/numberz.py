def is_number(x):
    """Check if x is a number.

    Parameters
    ----------
    x : object
        Object to check.

    Returns
    -------
    bool
        True if x is a number, False otherwise.

    """
    return isinstance(x, (int, float, complex))
