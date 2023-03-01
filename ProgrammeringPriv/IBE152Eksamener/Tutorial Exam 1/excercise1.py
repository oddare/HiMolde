"""1. A device measures the speed of cars running along a road with 3 lanes.
Any speed is allowed in lane 1.
The maximum speed in lane 3 is 70 Km per hour and it has no minimum speed.
In lane 2 the cars must run in speeds in the interval (60, 100).
Define a function that given a lane number an a speed it returns True if it is correct to run at that speed in that lane or False otherwise.
"""
def speedCheck(lane: int, speed: int) -> bool:
    if lane == 1:
        return True
    if lane == 2 and 60 < speed < 100:
        return True
    if lane == 3 and speed < 70:
        return True
    return False

print(speedCheck(2, 99))