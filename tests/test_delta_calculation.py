from typing import Tuple

from arrow import get
from assertpy import assert_that
from dateutil.relativedelta import relativedelta
from delta_calculation import calculate_delta
from pytest import mark

ONE_YEAR = relativedelta(years=12)
ONE_MONTH = relativedelta(months=1)
ONE_WEEK = relativedelta(weeks=1)
ONE_DAY = relativedelta(days=1)


@mark.parametrize(
    "birth_date, date_to_compare_to, expected_current_age",
    [
        ("2021-05-25", "2022-05-25", (1, 0, 0, 0)),
        ("2022-05-25", "2021-05-25", (-1, 0, 0, 0)),
        ("2024-02-28", "2024-03-28", (0, 1, 0, 0)),
        ("2024-02-29", "2025-02-28", (1, 0, 0, 0)),
        ("2024-02-28", "2025-02-28", (1, 0, 0, 0)),
        ("2024-02-28", "2024-02-29", (0, 0, 0, 1)),
        ("2024-02-28", "2024-03-01", (0, 0, 0, 2)),
        ("2023-02-28", "2023-03-01", (0, 0, 0, 1)),
        ("1983-08-24", "1984-08-24", (1, 0, 0, 0)),
        ("1983-07-21", "1983-08-21", (0, 1, 0, 0)),
        ("1983-07-21", "1983-07-28", (0, 0, 1, 0)),
        ("1983-08-24", "2022-05-29", (38, 9, 0, 5)),
        ("1983-08-24", "2022-06-05", (38, 9, 1, 5)),
    ],
)
def test__calculate_delta__works(
    birth_date: str,
    date_to_compare_to: str,
    expected_current_age: Tuple[int, int, int, int],
):
    actual_delta = calculate_delta(get(birth_date), get(date_to_compare_to))
    expected_delta = to_delta(*expected_current_age)

    assert_that(actual_delta).is_equal_to(expected_delta)


def to_delta(*nominal_values: int) -> relativedelta:
    years, months, weeks, days = nominal_values
    return relativedelta(years=years, months=months, weeks=weeks, days=days)
