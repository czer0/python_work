# example of a tuple
dimensions = (200, 50)
#dimensions[0] = 250 	# displays error when you try to change a tuple 
print(dimensions[0])
print(dimensions[1])
print("\n")

# print all values in a tuple with a for loop
dimensions = (200, 50)
for dimension in dimensions:
	print(dimension)

# writing over a tuple

dimensions = (200, 50)
print("\nOriginal dimensions:")
for dimension in dimensions: 
	print(dimension)
	
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
	print(dimension)
