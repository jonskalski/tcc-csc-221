# Given a line of text as input, output the number of characters
# excluding spaces, periods, exclamation points, or commas.

user_text = input()
num_char = 0

for character in user_text:
    if "a" <= character <= "z" or "A" <= character <= "Z" or character == "?":
        num_char += 1

print(num_char)