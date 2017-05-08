# two methods of creating a list from 1 to 1 million and then
# using min() max() and sum() 

numbers = list(range(0,1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

print("\n")

numbers = [value for value in range (1,1000001)]
print(min(numbers))
print(max(numbers))
print(sum(numbers))


