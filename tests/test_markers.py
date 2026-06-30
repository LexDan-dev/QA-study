import pytest
from study_cases.weekday import get_weekday


@pytest.mark.smoke
@pytest.mark.parametrize(
    "number, expected",
    [
        (1, "Понедельник"),
        (4, "Четверг"),
        (7, "Воскресенье"),
    ],
)
def test_weekday_smoke(number, expected):
    assert get_weekday(number) == expected


@pytest.mark.skip(reason="временно отключён")
def test_skipped_example():
    assert 1 == 2


@pytest.mark.xfail(reason="Упадет, так как 1 != 2")
def test_xfail_example():
    assert 1 == 2
