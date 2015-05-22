animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index =  animals.index("duck")  # Use index() to find "duck"

animals.insert(duck_index,"cobra")



print animals # Observe what prints after the insert operation

#######################

start_list = [5, 3, 1, 2, 4]
square_list = []

# Your code here!
for number in start_list:
    square_list.append(number ** 2)
   
print square_list

square_list.sort()    

print square_list

##########################

inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf'],
    'pocket' :['seashell','strange berry','lint']
    
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 

# Your code here
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')

inventory['gold'] += 50
