# Toll roads have different fees based on the time of day and on weekends. Write a function calc_toll() that has
# three parameters: the current hour of time (int), whether the time is morning (boolean), and whether the day
# is a weekend (boolean). The function returns the correct toll fee (float), based on the chart below.
#
# Weekday Tolls
#
# Before 7:00 am ($6.15)
# 7:00 am to 9:59 am ($7.95)
# 10:00 am to 2:59 pm ($6.90)
# 3:00 pm to 7:59 pm ($8.95)
# Starting 8:00 pm ($6.40)
# Weekend Tolls
#
# Before 7:00 am ($6.05)
# 7:00 am to 7:59 pm ($7.15)
# Starting 8:00 pm ($6.10)
# Ex: The function calls below, with the given arguments, will return the following toll fees:
#
# calc_toll(8, True, False) returns 7.95
# calc_toll(1, False, False) returns 6.90
# calc_toll(3, False, True) returns 7.15
# calc_toll(5, True, True) returns 6.05


def calc_toll(hour, is_morning, is_weekend):
    if is_weekend == True:
        if is_morning == True:
            if hour < 7:
                return 6.05
            else:
                return 7.15
        else:
            if hour < 8 or hour == 12:
                return 7.15
            else:
                return 6.10
    else:
        if is_morning == True:
            if hour < 7:
                return 6.15
            elif hour < 10:
                return 7.95
            else:
                return 6.90
        else:
            if hour < 3 or hour == 12:
                return 6.90
            elif hour < 8:
                return 8.95
            else:
                return 6.40

if __name__ == "__main__":
    print(calc_toll(8, True, False))
    print(calc_toll(1, False, False))
    print(calc_toll(3, False, True))
    print(calc_toll(5, True, True))
