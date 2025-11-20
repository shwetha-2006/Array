import sys
# If scores provided as command-line arguments
if len(sys.argv) > 1:
    scores = [int(x) for x in sys.argv[1:]]
else:
    print("No scores provided!")
    sys.exit(1)

# Calculations
total = sum(scores)
average = total / len(scores)
maximum = max(scores)
minimum = min(scores)

# Output
print("Scores =", scores)
print("Sum =", total)
print("Average =", average)
print("Maximum =", maximum)
print("Minimum =", minimum)




