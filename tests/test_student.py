import pytest
from study_cases.lead_n_student import Student, get_avg_grades


@pytest.mark.parametrize(
    "grades, expected",
    [
        ([4.0, 5.0, 3.0], 4.0),
        ([5.0, 5.0, 5.0], 5.0),
        ([2.0, 4.0], 3.0),
        ([], 0),
    ],
)
def test_get_avg_grades(grades, expected):
    student = Student("Тест", 20, grades)
    assert get_avg_grades(student) == expected
