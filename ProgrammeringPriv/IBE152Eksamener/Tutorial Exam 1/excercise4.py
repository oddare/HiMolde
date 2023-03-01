def number(num: int) -> str:
    string = 'OneTwoThrFouFivSixSevEigNinTenEleTweThi'
    return string[3*num-3:3*num]

print(number(2))