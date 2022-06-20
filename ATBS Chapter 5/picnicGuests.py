allGuests = {'Alice': {'apples': 5, 'prezels': 12},
	    'Bob': {'ham sandwiches': 3, 'apples': 2},
	    'Carol': {'cups': 3, 'apple pies': 1}}

def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():         # This 'for' loop iterates over the items (keys and values) in 'guests'. The guest's name is assigned to 'k', and his dictionary is assigned to 'v'.
        numBrought += v.get(item, 0)    # The values for that guest's keys are added in 'numBrought'. If a key does not exist in a guest's dictionary, the 'get()' method will then return 0 to 'numBrought'.
    return numBrought
    

print('Number of things being brought:')
print(' - Apples         ' + str(totalBrought(allGuests, 'apples')))        # 'allGuests' is the argument for the first parameter in 'totalBrought', and the key who's value is needed to be printed is assigned to the second.
print(' - Cups           ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes          ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies     ' + str(totalBrought(allGuests, 'apple pies')))




