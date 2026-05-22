"""계산기 테스트 (minimal)."""

from app.calculator import add, subtract


def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_subtract_positive_numbers():
    assert subtract(10, 3) == 7
