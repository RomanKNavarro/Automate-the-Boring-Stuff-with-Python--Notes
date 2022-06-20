# Chapter 4 Practice Projects



# Comma Code

def org(list):
        print(list[0:-1], 'and', list[-1]) # cannot get the brackets out the way

spam = ['hi','sweden', 'jew', 'micronesia']
org(spam)



# Character Picture Grid


grid = [['.','.','.','.','.','.'],
        ['.','0','0','.','.','.'],
        ['0','0','0','0','.','.'],
        ['0','0','0','0','0','.'],
        ['.','0','0','0','0','0'],
        ['0','0','0','0','0','.'],
        ['0','0','0','0','.','.'],
        ['.','0','0','.','.','.'],
        ['.','.','.','.','.','.']]


# the origin of grid[x][y] would be (0,0), which is at the upper left corner. This coordinate contains no value.
# The 'x' coordinate increases going right, and the 'y' coordinate increases going down. This graph has 6 X values going across and 9 Y values going down.
# The entire upper row of 'grid', made up soley of periods, would be grid[0], and the second row would be grid[1], and so on.



def dot(appel):
    for i in range(2,len(appel[0])):
        myStr = ''
        myStr += '111'
        print(myStr)

dot(grid)




# The i loop is iterating over the columns of grid. So you want to grab all values for the first column. The j loop therefore loops over the rows and appends the first column from each row to mystr. Print it, then rinse and repeat on to the 2nd column.
# The 'i' loop prints all the x values (of which there are six), while the second one prints the y values.
print()


def dot(appel):
    for i in range(0,len(appel[0])):
        myStr = ''
        for j in range(1,(len(appel))):
            myStr += appel[j][i]
        print(myStr)

dot(grid)



print()
print(grid[0][0],grid[1][0], grid[2][0],grid[3][0],grid[4][0],grid[5][0],grid[6][0],grid[7][0],grid[8][0])
print(grid[0][1],grid[1][1], grid[2][1],grid[3][1],grid[4][1],grid[5][1],grid[6][1],grid[7][1],grid[8][1])
print(grid[0][2],grid[1][2],grid[2][2],grid[3][2],grid[4][2],grid[5][2],grid[6][2],grid[7][2],grid[8][2])
print(grid[0][3],grid[1][3],grid[2][3],grid[3][3],grid[4][3],grid[5][3],grid[6][3],grid[7][3],grid[8][3])
print(grid[0][4],grid[1][4],grid[2][4],grid[3][4],grid[4][4],grid[5][4],grid[6][4],grid[7][4],grid[8][4])
print(grid[0][5],grid[1][5],grid[2][5],grid[3][5],grid[4][5],grid[5][5],grid[6][5],grid[7][5],grid[8][5])



        
       

                   























































