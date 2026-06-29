import pytest
from study_cases.weekday import get_weekday


@pytest.mark.parametrize(
    "number, expected",
    [
        (1, "Понедельник"),
        (2, "Вторник"),
        (3, "Среда"),
        (4, "Четверг"),
        (5, "Пятница"),
        (6, "Суббота"),
        (7, "Воскресенье"),
    ],
)
def test_get_weekday_valid(number, expected):
    assert get_weekday(number) == expected


@pytest.mark.parametrize("bad_number", [0, 8, -1, 100])
def test_get_weekday_invalid(bad_number):
    with pytest.raises(ValueError):
        get_weekday(bad_number)


def test_general_fixture_weekday(general_fixture):
    assert "фикстура из conftest.py" == general_fixture
