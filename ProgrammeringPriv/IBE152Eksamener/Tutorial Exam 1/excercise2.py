"""
Mary must decide between 2 boys. 
Both have their own strengths and weaknesses, and she cannot make her mind.
She left the decision to the daisy flower game: she will alternatively speak the number of the boy 1 and 2
while picking one petal of the flower for each num-ber. 
The number spoken on picking the last petal is the winner wooer.
But she doesn't want to destroy a daisy, and she knows you can help.
Write a function that receives the number of petals (a positive in-teger) in a daisy and
returns the number that would be spoken while picking off the last petal (1 or 2)
"""
def daisyGame(num: int) -> int:
    return ((num+1) % 2) + 1

print(daisyGame(4))