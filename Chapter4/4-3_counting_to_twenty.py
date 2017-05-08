# Using for loops to print the numbers 1 to 20

# Method 1 - create a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for numbers in numbers:
	print(numbers)

print ("\n")

# Method 2 - generate list
numbers = [value for value in range (1,21)]
for numbers in numbers:
	print(numbers)



