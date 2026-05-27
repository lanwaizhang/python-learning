def leap_year(year):
    """Leap year determination module.
"""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
