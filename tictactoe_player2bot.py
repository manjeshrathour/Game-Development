import numpy as np
import random as rn
grid= np.zeros((3,3),dtype=int)
turn=rn.randint(1,2)

def move_player():
    
    row=int(input("enter row from [0,1,2]-> "))
    col=int(input("enter col from [0,1,2]-> "))
    if(row not in [0,1,2] or col not in [0,1,2] or grid[row][col]!=0):
        print("Input is invalid")
        print("Give correct row and col")
        return move_player()
    else:
        return row,col

#for optimised bot move
def move_bot(grid):
    empty_cells = [(r, c) for r in range(3) for c in range(3) if grid[r, c] == 0]

    # checking for bot winnng
    for row, col in empty_cells:
        grid[row, col] = 1  
        if winner_check(grid) == 1:
            return row, col  # Winning move
        grid[row, col] = 0  # backtrack

    # block opponent
    for row, col in empty_cells:
        grid[row, col] = 2
        if winner_check(grid) == 2:
            return row, col  # Block move
        grid[row, col] = 0  

    # pos for winning count >=2 in next move
    for row, col in empty_cells:
        grid[row, col] = 1 
        win_count = 0
        for r, c in empty_cells:
            if (r, c) != (row, col): 
                grid[r, c] = 1    #second move
                if winner_check(grid) == 1:
                    win_count += 1
                grid[r, c] = 0  # Undo move
        grid[row, col] = 0  # Undo first move
        if win_count >= 2:
            return row, col

    # center move
    if (1,1) in empty_cells:
        return (1,1)

    # corner move
    corners = [(0,0), (0,2), (2,0), (2,2)]
    for corner in corners:
        if corner in empty_cells:
            return corner

    # random move
    choice = rn.randint(0, len(empty_cells) - 1)
    selected_move = empty_cells[choice]
    return selected_move


    
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

    if(turn==1):
        row,col=move_bot(grid)
    else:
        row,col=move_player()

    grid = update_grid(grid, row, col, turn)

    winner = winner_check(grid)
    if winner:
        break
    turn =3- turn
    count += 1


print("\nFinal Board:\n", grid)

if winner:
    if(winner==1):
        print("Winner is your bot sir")
    else:
        print("Wow you have won the game")
else:
    print("It's a draw! ")
