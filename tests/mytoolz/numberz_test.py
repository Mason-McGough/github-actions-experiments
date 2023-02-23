import pytest

from mytoolz import numberz


@pytest.mark.parametrize(
    "number, expected",
    [
        (1, True),
        (1.0, True),
        (1j, True),
        (1 + 1j, True),
        (True, True),
        (False, True),
        (None, False),
        ("1", False),
        ("1.0", False),
        ("1j", False),
        ("1 + 1j", False),
        ("True", False),
        ("False", False),
        ("None", False),
        ([1], False),
        (["1"], False),
        ({"1": 1}, False)
    ],
)
def test_is_number(number, expected):
    """Test is_number."""
    assert numberz.is_number(number) == expected
