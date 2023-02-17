from arrow import get
from assertpy import assert_that
from pytest import mark

from birthdayculator.next_birthday_calculation import calculate_next_birthday


@mark.parametrize(
    "birth_date, comparison_date, expected_next_birthday",
    [
        ("2021-05-25", "2022-05-25", "2023-05-25"),
        ("2022-05-25", "2021-05-25", "2022-05-25"),
        ("2024-02-28", "2024-03-28", "2025-02-28"),
        ("2024-02-29", "2025-02-28", "2026-02-28"),
        ("2024-02-28", "2025-02-28", "2026-02-28"),
        ("2024-02-28", "2024-02-29", "2025-02-28"),
        ("2024-02-28", "2024-03-01", "2025-02-28"),
        ("2023-02-28", "2023-03-01", "2024-02-28"),
        ("1983-08-24", "1984-08-24", "1985-08-24"),
        ("1983-07-21", "1983-08-21", "1984-07-21"),
        ("1983-07-21", "1983-07-28", "1984-07-21"),
        ("1983-08-24", "2022-05-29", "2022-08-24"),
    ],
)
def test__calculate_next_birthday__given_comparison_date__calculates_expected_birthday(
    birth_date: str,
    comparison_date: str,
    expected_next_birthday: str,
):
    next_birthday = calculate_next_birthday(birth_date, comparison_date)

    assert_that(next_birthday).is_equal_to(get(expected_next_birthday).date())
