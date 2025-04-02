import numpy as np
import random as rn

def updatemaze(move):
    global start  # To modify start correctly
    new_pos = start.copy()
    
    if move == "left" and start[1] > 0 and maze[start[0], start[1] - 1] != 1:
        new_pos[1] -= 1
    elif move == "right" and start[1] < 9 and maze[start[0], start[1] + 1] != 1:
        new_pos[1] += 1
    elif move == "down" and start[0] < 9 and maze[start[0] + 1, start[1]] != 1:
        new_pos[0] += 1
    elif move == "up" and start[0] > 0 and maze[start[0] - 1, start[1]] != 1:
        new_pos[0] -= 1
    elif move == "diaglup" and start[0] > 0 and start[1] > 0 and maze[start[0] - 1, start[1] - 1] != 1:
        new_pos[0] -= 1
        new_pos[1] -= 1
    elif move == "diagrup" and start[0] > 0 and start[1] < 9 and maze[start[0] - 1, start[1] + 1] != 1:
        new_pos[0] -= 1
        new_pos[1] += 1
    elif move == "diagldown" and start[0] < 9 and start[1] > 0 and maze[start[0] + 1, start[1] - 1] != 1:
        new_pos[0] += 1
        new_pos[1] -= 1
    elif move == "diagrdown" and start[0] < 9 and start[1] < 9 and maze[start[0] + 1, start[1] + 1] != 1:
        new_pos[0] += 1
        new_pos[1] += 1

    # Update position in maze
    if np.array_equal(new_pos, start):  
        print("Move blocked!")
    else:
        maze[start[0], start[1]] = 0  # Clear previous position
        start[:] = new_pos
        maze[start[0], start[1]] = 8  # Mark new position

    return maze

# Initialize maze
maze = np.zeros((10, 10))

# Populate maze with obstacles (1)
for i in range(10):  # Fixed range to include all rows
    for j in range(10):  # Fixed range to include all columns
        if rn.randint(0, 10) > 6:  # Less density of obstacles
            maze[i, j] = 1

# Start and End positions
start = np.array([rn.randint(0, 5), rn.randint(0, 9)])
end = np.array([rn.randint(6, 9), rn.randint(0, 9)])


# Ensure start and end points are not blocked
maze[start[0], start[1]] = 8  
maze[end[0], end[1]] = 9  

print("Start position:", start)
print("End position:", end)
print(maze)

# Game loop
key = input("Move using W, A, S, D (diagonal: Q, E, Z, C), X to exit: ").lower()
while key != "x":
    if np.array_equal(start, end):
        print("Game Over! You reached the destination.")
        break

    moves = {"a": "left", "d": "right", "s": "down", "w": "up",
             "q": "diaglup", "e": "diagrup", "z": "diagldown", "c": "diagrdown"}

    if key in moves:
        print(f"Moving {moves[key]}")
        maze = updatemaze(moves[key])
        print(maze)
    else:
        print("Invalid key! Use W, A, S, D (Q, E, Z, C for diagonals).")
    if np.array_equal(start, end):
        print("Game Over! You reached the destination.")
        break

    key = input("Your move: ").lower()

print("Game ended.")

