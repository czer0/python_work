# example of copying a list

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods #[:] remove hash to have it work as intended

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("\nMy favorite food are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
