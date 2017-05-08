# Three methods to accomplish the same result. 
# The list comprehension method is the preferred method.

squares = []
for value in range(1,11):
	square = value**2
	squares.append(square)
print(squares)

# More concise method
squares = []
for value in range(1,11):
	squares.append(value**2)

print("\n" + str(squares))

# list comprehension method
squares = [value**2 for value in range(1,11)]
print(squares)
