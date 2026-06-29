import pytest
from study_cases.lead_n_student import Student, get_avg_grades


@pytest.fixture
def sample_student():
    return Student("Анна", 20, [4.0, 5.0, 3.0])


def test_get_avg_grades(sample_student):
    assert get_avg_grades(sample_student) == 4.0
