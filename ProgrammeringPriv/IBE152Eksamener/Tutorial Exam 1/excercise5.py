"""
Write a function that given the current day of the week in string format 
("Mon", "Tue", etc.) and a number n, returns a string corresponding 
to the day of the week of the day after n days.

Example: day_of_week("Wed", 9) -> "Fri"
"""
def weekDay(day: str, num: int) -> int:
    week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    val =  (week.index(day) + num) % 7
    return week[val]

print(weekDay('Tue', 6))