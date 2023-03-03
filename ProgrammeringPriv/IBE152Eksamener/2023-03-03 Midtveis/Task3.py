def insert_str(target: str, string: str, position: int) -> str:
    '''
    Adds string to given position of target

    Args:
    - target, str, the text to add to
    - string, str, the string to be added to target
    - position, int, the position at which to add string to target

    Returns:
    - The result of string being added at the given position in target
    '''
    start = target[:position]
    end = target[position:]

    return f'{start}{string}{end}'



target = 'Here'
target = insert_str(target, ' the', 4)
target = insert_str(target, ' comes', 4)
target = insert_str(target, ' duck', 14)
print(target)