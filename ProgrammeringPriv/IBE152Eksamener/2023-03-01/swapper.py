def swapper(s: str, c: str, pos: int) -> str:
    first = s[0:pos]
    end = s[pos-1: -1]
    return f'{first}{c}{end}'


print(swapper('....', 'A', 2)) # -> ..A..