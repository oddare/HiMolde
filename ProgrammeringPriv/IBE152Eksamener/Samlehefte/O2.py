def clock(seconds: int) -> str:
    hours = int((seconds // 3600))
    minutes = int((seconds // 60) % 60)
    seconds = int(seconds % 60)
    return f''


print(clock(3600*2.87))
