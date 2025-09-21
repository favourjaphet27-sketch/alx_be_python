# Prompt the user for input
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Draw the square pattern
while row < size:
    for col in range(size):
        print("*", end=" ")
    print()  # move to the next row
    row += 1
