from add import add
from assertpy import assert_that


def test__add():
    assert_that(add(1, 1)).is_equal_to(2)
