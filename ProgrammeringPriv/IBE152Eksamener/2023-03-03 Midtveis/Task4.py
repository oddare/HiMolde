def display(num: int) -> list:
    '''
    Takes the number of the day and returns a list of string for use in a
    7-digit display. If the value is less than 10, adds a 0 in front.

    Args:
    - num, integer, the day of the month

    Returns:
    - A list of strings showing two 7 digit displays for each number
    '''
    digits = [
        '1111110', #0
        '1100000', #1
        '1011011', #2
        '1110011', #3
        '1100101', #4
        '0110111', #5
        '0111111', #6
        '1100010', #7
        '1111111', #8
        '1110111', #9
    ]
    string = str(num).zfill(2)
    list = [digits[int(string[0])], digits[int(string[1])]]
    return list

print(display(7))