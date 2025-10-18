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
