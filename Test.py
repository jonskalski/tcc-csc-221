# Analyze a week's worth of step counts
def analyze_steps(steps_list):
    # steps_list is a list of 7 integers (one per day)
    total_steps = sum(steps_list)
    average_steps = total_steps / len(steps_list)
    max_steps = max(steps_list)
    return total_steps, average_steps, max_steps


# Main program
print("Enter your step count for each day of the week.")
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
weekly_steps = []

for day in days:
    steps = int(input(f"{day}: "))
    weekly_steps.append(steps)


total, average, highest = analyze_steps(weekly_steps)

print("Weekly step summary:")
print(f"Total steps: {total}")
print(f"Average steps per day: {average:.0f}")
print(f"Highest step count in a day: {highest}")
