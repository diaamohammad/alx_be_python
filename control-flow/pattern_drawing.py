# Ask the user for input
size = int(input("Enter a positive integer for the pattern size: "))

# Ensure the size is positive
while size <= 0:  # Ensure the input is positive
    size = int(input("Please enter a positive integer: "))

# Start drawing the square
row = 0  # Variable to control the number of rows

# Use a while loop to repeat for the number of rows
while row < size:
    # Use a for loop to print the columns (stars) in the same row
    for col in range(size):  # col means column
        print("*", end="")  # end="" prevents moving to the next line
    print()  # Move to the next line after printing all stars in the row
    row += 1  # Increment the row count
