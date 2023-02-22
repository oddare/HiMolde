def timeToDestination(busSchedule: list, time: int, timeLimit: int) -> list:
    timeschedule = []
    for n in range(len(busSchedule)):
        if busSchedule[n][1] >= time:
            timeschedule.append(busSchedule[n])
    limitschedule = []
    for n in range(len(timeschedule)):
        if timeschedule[n][2] <= timeLimit:
            limitschedule.append(timeschedule[n])
    return limitschedule

buses = [("701a", 10, 20), ("702a", 20, 15), ("703a", 0, 10), ("704", 38, 13)]
now = 5
limit = 50

print(timeToDestination(buses, now, limit))