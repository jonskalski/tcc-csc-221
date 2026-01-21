# Given a sorted list of integers, output "Middle item: " followed by the middle integer. Assume the number
# of integers is always odd.
# The maximum number of inputs for any test case should not exceed 9. If exceeded, output "Too many inputs".


number_list = input()
nums = number_list.split()

num_list = []

for i in nums:
    num_list.append(i)

list_length = len(num_list)

if list_length > 9:
    print("Too many inputs")
else:
    mid_num = (list_length // 2)
    print(f"Middle item: {num_list[mid_num]}")
