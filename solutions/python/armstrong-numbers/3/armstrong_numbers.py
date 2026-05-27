"""This module provides a function to print the current Python version."""
def is_armstrong_number(number):
    digits = [int(digit_char) for digit_char in str(number)]
    power = len(digits)
    return sum(digit**power for digit in digits) == number
                
                
