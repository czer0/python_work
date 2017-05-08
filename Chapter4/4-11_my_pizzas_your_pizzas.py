# example of two different lists with a 
# variable appended to friend_pizza then output printed for comparison

pizzas = ['hawaiian', 'supreme', 'veggie', 'greek', 'meat']
friend_pizzas = ['hawaiian', 'supreme', 'veggie', 'greek', 'meat']
friend_pizzas.append('donair')

for pizza in pizzas:
	print("I like " + pizza.title() + " pizza." )

for pizza in friend_pizzas:
	print("he likes " + pizza.title() + " pizza." )


print("\n REALLY like pizza")

