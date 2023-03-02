def clock(seconds: int) -> str:
    hours = (seconds // 3600)
    minutes = (seconds // 60) % 60
    seconds = seconds % 60
    return f''


print(clock(3600*2.87))