"""
You're given a sorted list of numbers in a sequence from 1 to n with one of the numbers 
missing (number 1 is always present). 
Design a function that takes a sorted list as argument and returns the 
number that is missing from the list. 
(Application of Gauss method for the summation 1..n)
"""
def numCheck(sortedList: list) -> int:
    endNum = len(sortedList) + 1
    gauss = endNum / 2 * (endNum + 1)
    listSum = sum(sortedList) #Can we use sum()?
    return int(gauss - listSum)


list = [1, 2, 3, 4, 6, 7, 8, 9, 10] #Missing 5

print(numCheck(list))