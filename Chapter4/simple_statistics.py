#line 6 prints each value on a seperate line
#line 8 prints all values on the same line with no spacing
#line 10 just adds all values together
 
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(str(min(digits)) + "\n" + str(max(digits)) + "\n" + str(sum(digits)))
print("\n")

print(str(min(digits)) + str(max(digits)) + str(sum(digits)))
print("\n")

print(min(digits) + max(digits) + sum(digits))
