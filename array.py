import sys
sys.stdout.write("How many scores do you want to enter? ")
n = int(sys.stdin.readline().strip())
scores = []
for i in range(n):
    sys.stdout.write(f"Enter score {i+1}: ")
    value = int(sys.stdin.readline().strip())
    scores.append(value)

# Calculations
total = sum(scores)
average = total / len(scores)
maximum = max(scores)
minimum = min(scores)

# Output
print("\nScores =", scores)
print("Sum =", total)
print("Average =", average)
print("Maximum =", maximum)
print("Minimum =", minimum)




