def weekDay(day: str, num: int) -> int:
    week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    val =  (week.index(day) + num) % 7
    return 

print(weekDay('Tue', 1))