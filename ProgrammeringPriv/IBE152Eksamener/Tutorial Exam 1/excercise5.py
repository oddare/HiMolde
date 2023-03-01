def weekDay(day: str, num: int) -> int:
    list = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    val =  list.index(day)
    return val

print(weekDay('Tue', 1))