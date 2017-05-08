# Overwriting a tuple with new items 

buffet_items = ('toast', 'eggs', 'pancakes', 'fruit', 
				'bacon') #breakfast menu
#~ buffet_items[0] = 'ham' # error generation test
#~ buffet_items.append('ham') # error generation test
print("Breakfast menu:")
for buffet_breakfast in buffet_items:
    print(buffet_breakfast.title())

print("\n")
    
buffet_items = ('hamburger', 'fries', 'garden salad', 
				'coleslaw', 'chicken fingers') #lunch menu
print("Lunch menu:")
for buffet_lunch in buffet_items:
    print(buffet_lunch.title())
