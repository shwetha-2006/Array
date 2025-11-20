import sys 
n = int(input("How many scores do you want to enter? "))

scores = []

# Take scores one by one
for i in range(n):
    value = int(input(f"Enter score {i+1}: "))
    scores.append(value)

# Calculate values
total = sum(scores)
average = total / len(scores)


# Print results
print("\nScores =", scores)
print("Sum =", total)
print("Average =", average)
