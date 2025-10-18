# Golf scores record the number of strokes used to get the ball in the hole. The expected number of strokes varies from
# hole to hole and is called par (possible values: 3, 4, or 5). Each score's name is based on the actual strokes taken
# compared to par:
#
# Given two integers that represent the number of strokes used and par, write a program that prints the appropriate
# score name. Print "Error" at the end of the output if par is not 3, 4, or 5,
# or if the score's name is not "Eagle", "Birdie", "Par", or "Bogey".

strokes = int(input())
par = int(input())

score = par - strokes

if par not in (3,4,5):
    type = "Error"
elif score == 2:
    type = "Eagle"
elif score == 1:
    type = "Birdie"
elif score == 0:
    type = "Par"
elif score == -1:
    type = "Bogey"
else:
    type = "Error"


print(f"Par {par} in {strokes} strokes is {type}")
