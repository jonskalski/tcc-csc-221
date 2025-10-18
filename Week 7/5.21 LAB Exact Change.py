change = int(input())

if change == 0:
    print("No change")

dollar = 0
quarter = 0
dime = 0
nickel = 0
penny = 0

while change >= 100:
    change -= 100
    dollar += 1
while change >= 25:
    change -= 25
    quarter += 1
while change >= 10:
    change -= 10
    dime += 1
while change >= 5:
    change -= 5
    nickel += 1
while change >= 1:
    change -= 1
    penny += 1

if dollar > 0:
    if dollar == 1:
        print("1 Dollar")
    else:
        print(f"{dollar} Dollars")
if quarter > 0:
    if quarter == 1:
        print("1 Quarter")
    else:
        print(f"{quarter} Quarters")
if dime > 0:
    if dime == 1:
        print("1 Dime")
    else:
        print(f"{dime} Dimes")
if nickel > 0:
    if nickel == 1:
        print("1 Nickel")
    else:
        print(f"{nickel} Nickels")
if penny > 0:
    if penny == 1:
        print("1 Penny")
    else:
        print(f"{penny} Pennies")
