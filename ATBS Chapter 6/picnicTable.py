def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS' .center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth,'.') + str(v).rjust(rightWidth, '.'))    # This will print the item names (k) to the right and teir quantity (v) to the left
picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 10, 10)

