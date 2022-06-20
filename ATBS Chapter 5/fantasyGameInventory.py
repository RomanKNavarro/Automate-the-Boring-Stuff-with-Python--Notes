# inventory.py
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():          # the keys are represented by k and the values by v
        item_total += v                     # All of the dictionary's values are stored in item_total
        print(str(v) + ' ' + k)             # prints the all of the values along with the keys
    print('Total number of items: ' + str(item_total))  # the amount of items in item_total is printed
displayInventory(stuff)
print()



# list items to dictionaries

# Dragon's loot
def addToInventory(inventory, addedItems):
    for items in addedItems:                # All of the items in 'addedItems'(list) are added to 'inventory'(dictionary) by 
        inventory.setdefault(items, 0)      # using setdefault to add the list items to their respective keys in the dictionary
        inventory[items] += 1               # The value of the keys is incremented by one for each of it's item in the list
    return inventory
        
    
inv = {'gold coin': 42, 'rope': 1}
displayInventory(inv)                                                   # All of the values in 'inv' will be printed using the displayInventory() function
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']  
inv = addToInventory(inv, dragonLoot)                                   # Using the addToInventory() function, the items in dragonLoot are added to the keys
displayInventory(inv)                                                   # in the inv dictionary, increasing their integer value















