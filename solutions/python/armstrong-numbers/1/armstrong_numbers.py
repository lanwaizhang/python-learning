def is_armstrong_number(number):
    digits = [int(d) for d in str(number)]
    power = len(digits)
    return sum(d**power for d in digits) == number
                
                
