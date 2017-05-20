# Start with a list of sandwich orders,
# and an empty list to hold finished orders
sandwich_orders = [
    'ruben', 'pastrami', 'chicken', 'pastrami', 'blt', 
    'peanut butter', 'pastrami', 'baloney'
                    ]
finished_sandwiches = []

# Remove all instances of pastrami from the orders list.
# Print notification that there is no pastrami.                    
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    
print("We are currently out of Pastrami\n")

# Verify each sandwich ordered until there are no more orders.
# Move each finished order to the finished sandwiches list.     
while sandwich_orders:
    order = sandwich_orders.pop()
    
     
    print("A " + order.title() + " sandwich has been ordered")
    finished_sandwiches.append(order)

print("\n")

# Display all finished sandwiches
for finished_sandwiches in finished_sandwiches:
    print("The " + finished_sandwiches.title() + " sandwich is finished")

    
