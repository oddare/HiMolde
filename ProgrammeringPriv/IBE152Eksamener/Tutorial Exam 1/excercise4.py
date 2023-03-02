"""
Write a program that asks the user for a number from 1 to 13 and print the three 
first letters of the name of the number as a string. 
To do this, return the appropriate sub-string of the string  
"OneTwoThrFouFivSixSevEigNinTenEleTweThi".
"""
def number(num: int) -> str:
    string = 'OneTwoThrFouFivSixSevEigNinTenEleTweThi'
    return string[3*num-3:3*num]

print(number(10))