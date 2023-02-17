from delta_calculation import Age


def to_age(*nominal_values: int) -> Age:
    years, months, weeks, days = nominal_values

    return Age(years=years, months=months, weeks=weeks, days=days)
