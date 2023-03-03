def farmYield(N: int, values: list) -> int:
    '''
    Checks if there are enough eggs to make the trip worthwhile, if there is
    then calculates the total amount of survivors.
    Takes the survivors and checks if they are between M1 (value[3]) and
    M2 (value[4]). If any eggs have made it, they can be sold in pairs of three
    for one golden bar. If less than three makes it, nothing is earned.

    Args:
    - N, integer, the starting value
    - values, list, a list of which to check conditions agains

    Returns:
    - An integer showing the farms yield
    '''
    H1 = values[0]
    H2 = values[1]
    K = values[2]
    M1 = values[3]
    M2 = values[4]

    if N < H1:
        return 0
    
    if N > H2:
        N = H2

    if N > K:
        N = K

    if M1 < N < M2:
        return N // 3
    
    return 0


print(farmYield(19, [10, 14, 4, 5, 6]))     #0
print(farmYield(100, [10, 14, 4, 5, 16]))   #0
print(farmYield(100, [10, 14, 4, 0, 16]))   #1