def leap_year(year):
    """Leap year determination module.

This module provides a single function `is_leap_year()` that returns whether a
given year is a leap year according to the Gregorian calendar.

Examples:
    >>> is_leap_year(2000)
    True
    >>> is_leap_year(1900)
    False
"""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
