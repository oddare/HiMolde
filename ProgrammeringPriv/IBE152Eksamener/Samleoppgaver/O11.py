def secret(paragraph: str, pairs: list) -> str:
    in1 = paragraph[pairs[0][0]:pairs[0][1]+1]
    in2 = paragraph[pairs[1][0]:pairs[1][1]+1]
    in3 = paragraph[pairs[2][0]:pairs[2][1]+1]
    return f'{in1}{in2}{in3}'


print(secret('Batman will try', [[0, 0], [4, 4], [9, 10]])) #Ball
print(secret('Snow or chocolate is the question', [[1, 3], [17, 20], [13, 16]])) #now is late