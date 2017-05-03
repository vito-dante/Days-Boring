
def numbers_digit(number: int) -> int:
    digits_cont = 0
    while number >= 1:
        number /= 10
        digits_cont += 1
    return digits_cont
