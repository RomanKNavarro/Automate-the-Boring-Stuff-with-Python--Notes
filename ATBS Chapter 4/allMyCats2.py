# allMyCats2.py: (with list)

catNames = []   # An empty list
while True:
    print('Enter the name of cat ' + str(len(catNames)) +   # The str() will print the cat number and the '+1' is to start with 'cat 1' rather than 'cat 0'.
          ' (Or enter nothing to stop.):')                      # This space is for compactness
    name = input()
    if name == '':
        break
    catNames = catNames + [name]    # The names given are turned into items for the list 'catNames'.
print('The cat names are:')
for name in catNames:
    print('  ' + name)              # This will print the items in 'catNames', spaced twice to the left
    print(catNames + ['ginger'])
