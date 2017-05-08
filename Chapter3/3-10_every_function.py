print("Current available transports:")
transport = ['car', 'truck', 'train', 'boat', 
            'plane', 'motocycle']
print(transport)
print("Current number of available transports:")
print(len(transport))
print("\nToday I will take the " + transport[0].title() + ".\n")

transport_in_use = transport.pop(0)
print("Since the car is in use the current available transports are:")
print(transport)
print("Current number of available transports:")
print(len(transport))
print("\n")

transport.insert(0, 'space shuttle')
transport.insert(1, 'dog sled')
print("Several new methods of transport have become available: " 
     + transport[0].title() + ", " + transport[1].title())
print("Current available transports:")
print(transport)
print("Current number of available transports:")
print(len(transport))
print("\n")

transport.append('horse')
print("A Horse has been purchased and is now available for use.")

print("Current available transports:")
print(transport)
print("Current number of available transports:")
print(len(transport))
print("\n")

dead_animal = 'horse'
transport.remove(dead_animal)
print("The " + dead_animal.title() + 
     " has died of spontanious combustion and is no longer available")

print("Current available transports:")
print(transport)
print("Current number of available transports:")
print(len(transport))
print("\n") 

print("The space Shuttle to expensive to operate and has been sold")
del transport[0]
print(transport)
print("Current number of available transports:")
print(len(transport))
print("\n") 

broken_down = transport.pop()
print("The " + broken_down.title() + 
     " is now in the shop and unavailble for use")

print(transport)
print("Current number of available transports:")
print(len(transport))
print("\n") 

print("Alpabetical listing of total transports available:") 
print(sorted(transport))
print("\n")

print("Reverse alpabetical listing of total transports available:") 
transport.sort(reverse=True)
print(transport)
print("\n")

