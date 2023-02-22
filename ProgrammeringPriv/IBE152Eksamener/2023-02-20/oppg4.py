def timeToDestination(busSchedule: list, time: int, timeLimit: int) -> list:
    timeschedule = []
    for n in range(len(busSchedule)):
        destinationTime = busSchedule[n][1] + busSchedule[n][2]
        if busSchedule[n][1] >= time and destinationTime <= timeLimit:
            timeschedule.append(busSchedule[n])
    return timeschedule

buses = [("701a", 10, 20), ("702a", 20, 15), ("703a", 0, 10), ("704", 38, 13)]
now = 5
limit = 50

print(timeToDestination(buses, now, limit))