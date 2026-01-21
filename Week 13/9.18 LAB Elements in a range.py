Write a program that first gets a list of integers from input. That list is followed by two more integers representing
lower and upper bounds of a range. Your program should output all integers from the list that are within that
range (inclusive of the bounds).

For coding simplicity, follow each output integer by a comma, even the last one. Do not end with newline.






int_input = input()
bound_input = input()

int_list = []
bound_list = []

for j in int_input.split():
    int_list.append(int(j))

for k in bound_input.split():
    bound_list.append(int(k))

bound_low = int(bound_list[0])
bound_high = int(bound_list[1])

final_list = []

for i in int_list:
    if i >= bound_low and i <= bound_high:
        final_list.append(i)

for m in final_list:
    print(f"{m},", end="")

