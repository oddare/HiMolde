def servings(guests: int) -> list:
    '''
    Calculates the minimum amount of cakes and champagne bottles required to
    serve all of the attending guests

    Args:
    - guests, integer, the amount of guests attending

    Returns:
    - The amount of cakes and champagne bottles required to serve the guests,
      as a list
    '''

    cakes = guests // 6
    if guests % 6 > 0:
        cakes += 1

    champagne = guests // 5
    if guests % 5 > 0:
        champagne += 1
    return [cakes, champagne]

print(servings(10))