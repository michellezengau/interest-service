import pytest

from app.calculator import compound_interest


def test_two_years_at_five_percent():
    assert compound_interest(1000, 5, 2) == 1102.5


def test_zero_rate_returns_principal():
    assert compound_interest(1005, 0, 10) == 1000


@pytest.mark.parametrize("p, r, y", [(0, 5, 1), (1000, -1, 1), (1000, 5, 0)])
def test_invalid_inputs_raise(p, r, y):
    with pytest.raises(ValueError):
        compound_interest(p, r, y)
