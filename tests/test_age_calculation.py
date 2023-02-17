from __future__ import annotations

from typing import Tuple

from age_calculation import calculate_age
from arrow import Arrow, get
from assertpy import assert_that
from freezegun import freeze_time
from pytest import mark

from tests.utils_test import to_age


@mark.parametrize(
    "birthday_input, date_to_compare_to_input, expected_age",
    [
        (get("2021-05-25"), get("2022-05-25"), (1, 0, 0, 0)),
        (get("2022-05-25"), get("2021-05-25"), (-1, 0, 0, 0)),
        (get("2024-02-28"), get("2024-03-28"), (0, 1, 0, 0)),
        (get("2024-02-29"), get("2025-02-28"), (1, 0, 0, 0)),
        (get("2024-02-28"), get("2025-02-28"), (1, 0, 0, 0)),
        (get("2024-02-28"), get("2024-02-29"), (0, 0, 0, 1)),
        (get("2024-02-28"), get("2024-03-01"), (0, 0, 0, 2)),
        (get("2023-02-28"), get("2023-03-01"), (0, 0, 0, 1)),
        (get("1983-08-24"), get("1984-08-24"), (1, 0, 0, 0)),
        (get("1983-07-21"), get("1983-08-21"), (0, 1, 0, 0)),
        (get("1983-07-21"), get("1983-07-28"), (0, 0, 1, 0)),
        (get("1983-08-24"), get("2022-05-29"), (38, 9, 0, 5)),
        (get("1983-08-24"), get("2022-06-05"), (38, 9, 1, 5)),
    ],
)
def test__calculate_age__given_two_dates__correctly_calculates_age(
    birthday_input: Arrow | str,
    date_to_compare_to_input: Arrow | str,
    expected_age: Tuple[int, int, int, int],
):
    calculated_age = calculate_age(birthday_input, date_to_compare_to_input)

    assert_that(calculated_age).is_equal_to(to_age(*expected_age))


@mark.parametrize(
    "birthday_input, date_to_compare_to_input, expected_age",
    [
        ("2021-05-25", "2022-05-25", (1, 0, 0, 0)),
        ("2021-05-25", get("2022-05-25"), (1, 0, 0, 0)),
        (get("2021-05-25"), "2022-05-25", (1, 0, 0, 0)),
        (get("2021-05-25"), get("2022-05-25"), (1, 0, 0, 0)),
    ],
)
def test__calculate_age__given_different_types__handles_the_same_way(
    birthday_input: Arrow | str,
    date_to_compare_to_input: Arrow | str,
    expected_age: Tuple[int, int, int, int],
):
    calculated_age = calculate_age(birthday_input, date_to_compare_to_input)

    assert_that(calculated_age).is_equal_to(to_age(*expected_age))


@mark.parametrize(
    "birthday_input, expected_age",
    [
        ("2021-05-25", (1, 8, 3, 0)),
        ("2022-05-25", (0, 8, 3, 0)),
        ("2023-02-15", (0, 0, 0, 0)),
        ("2024-02-28", (-1, 0, -1, -6)),
        ("2024-02-29", (-1, 0, -2, 0)),
        ("2023-02-28", (0, 0, -1, -6)),
        ("1983-08-24", (39, 5, 3, 1)),
        ("1983-07-21", (39, 6, 3, 4)),
        ("1982-08-24", (40, 5, 3, 1)),
    ],
)
@freeze_time("2023-02-15")
def test__calculate_age__using_now(birthday_input: Arrow | str, expected_age: Tuple[int, int, int, int]):
    calculated_age = calculate_age(birthday_input)

    assert_that(calculated_age).is_equal_to(to_age(*expected_age))
