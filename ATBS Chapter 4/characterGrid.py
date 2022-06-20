grid = [['.', '.', '.', '.', '.', '.'], # Each list and inner value in grid have coordinates. For example, the first list would be grid[0],
        ['.', '0', '0', '.', '.', '.'], # the second one grid[1], and so on. The first value of the first list would be grid[0][0], then the
        ['0', '0', '0', '0', '.', '.'], # second value of the second list would be grid[1][1], and so on.
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

for x in range(0, len(grid[0])):        # The length of grid[0] is 6
    str = ''                            
    for y in range(0, len(grid)):       # The length of grid is 9
        str = str + grid[y][x]
    print(str)

# This is the output:

#   ..00.00..                   The length of each line is 9 characters (y)
#   .0000000.                   the length of all the lines is 6 characters (x)
#   .0000000.
#   ..00000..
#   ...000...
#   ....0....

# Once the program has iterated through the values in the first list in grid, it iterates through the the rest of the lists in grid. X represents
# the values in the first list, and Y represents the rest of the list. For every value in X, each value below it gets printed, resulting in
# the vertical image.
            
                
            
            
            
            

       
       
       
        

