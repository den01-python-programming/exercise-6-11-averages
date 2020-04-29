import pytest
from src.grade_register import GradeRegister

def test_exercise():
    register = GradeRegister()
    register.add_grade_based_on_points(93)
    register.add_grade_based_on_points(91)

    assert register.average_of_grades() == 5
    assert register.average_of_points() == 92
