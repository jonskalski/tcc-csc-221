highway_number = int(input())

if highway_number % 2 == 0:
    direction = ("east/west")
else:
    direction = ("north/south")

if 1 < highway_number <= 99:
    print(f"I-{highway_number} is primary, going {direction}")
elif 101 < highway_number <= 999 and highway_number % 100 != 0:
    feed = (highway_number - ((highway_number // 100)*100))
    print(f"I-{highway_number} is auxillary, serving {feed}, going {direction}")
else:
    print(f"{highway_number} is not a valid interstate highway number.")


