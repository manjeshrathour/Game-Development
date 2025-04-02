import numpy as np
import random as rn
grid= np.zeros((3,3),dtype=int)
turn=rn.randint(1,2)

def move():
    
    row=int(input("enter row from [0,1,2]-> "))
    col=int(input("enter col from [0,1,2]-> "))
    if(row not in [0,1,2] or col not in [0,1,2] or grid[row][col]!=0):
        print("Input is invalid")
        print("Give correct row and col")
        return move()
    else:
        return row,col

def update_grid(grid,row,col,player):
    grid[row,col]=player
    return grid

def winner_check(grid):
    for i in range(3):
        if(grid[i][0]==grid[i][1]==grid[i][2] and grid[i][0]>0):
            return grid[i][0]
        if(grid[0][i]==grid[1][i]==grid[2][i] and grid[0][i]>0):
            return grid[0][i]
    
    if(grid[0][0]==grid[1][1]==grid[2][2] and grid[1][1]>0):
        return grid[1][1]
    if(grid[0][2]==grid[1][1]==grid[2][0] and grid[1][1]>0):
        return grid[1][1]
        
    return 0
count = 0
winner=0;
while (count<9):
    print("\nCurrent Board:\n", grid)
    print("Current player: ", turn)
    
    row, col = move()
    grid = update_grid(grid, row, col, turn)

    winner = winner_check(grid)
    if winner:
        break
    turn =3- turn
    count += 1


print("\nFinal Board:\n", grid)

if winner:
    print(f"Winner of the game is-> Player  ", winner)
else:
    print("It's a draw! ")
