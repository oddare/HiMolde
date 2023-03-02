def secret(paragraph: str, pairs: list) -> str:
    in1 = paragraph[pairs[0][0]:pairs[0][1]+1]
    in2 = 2
    in3 = 2


print(secret('Batman will try', [[0, 0], [4, 4], [9, 10]])) #Ball