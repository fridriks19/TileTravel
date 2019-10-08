# Constants
NORTH = 'n'
EAST = 'e'
SOUTH = 's'
WEST = 'w'

def move(direction, col, row):
    ''' Returns updated col, row given the direction '''
    if direction == NORTH:
        row += 1
    elif direction == SOUTH:
        row -= 1
    elif direction == EAST:
        col += 1
    elif direction == WEST:
        col -= 1
    return(col, row)    

def is_victory(col, row):
    ''' Return true is player is in the victory cell '''
    return col == 3 and row == 1 # (3,1)

def print_directions(directions_str):
    print("You can travel: ", end='')
    first = True
    for ch in directions_str:
        if not first:
            print(" or ", end='')
        if ch == NORTH:
            print("(N)orth", end='')
        elif ch == EAST:
            print("(E)ast", end='')
        elif ch == SOUTH:
            print("(S)outh", end='')
        elif ch == WEST:
            print("(W)est", end='')
        first = False
    print(".")
        
def find_directions(col, row):
    ''' Returns valid directions as a string given the supplied location '''
    if col == 1 and row == 1:   # (1,1)
        valid_directions = NORTH
    elif col == 1 and row == 2: # (1,2)  # þetta tile 
        valid_directions = NORTH+EAST+SOUTH
    elif col == 1 and row == 3: # (1,3)
        valid_directions = EAST+SOUTH
    elif col == 2 and row == 1: # (2,1)
        valid_directions = NORTH
    elif col == 2 and row == 2: # (2,2)  #þetta 
        valid_directions = SOUTH+WEST
    elif col == 2 and row == 3: # (2,3)   # þetta 
        valid_directions = EAST+WEST
    elif col == 3 and row == 2: # (3,2) # þetta 
        valid_directions = NORTH+SOUTH
    elif col == 3 and row == 3: # (3,3)
        valid_directions = SOUTH+WEST
    return valid_directions

def lever(col, row):
    tupla = (col, row)
    if tupla == (1, 2):
        user_input = input("Pull a lever (y/n): ")
        if user_input == "y" or user_input == "Y":
            return True 
        else:
            return False

    elif tupla == (2, 2):
        user_input = input("Pull a lever (y/n): ")
        if user_input == "y" or user_input == "Y":
            return True
        else:
            return False

    elif tupla == (2, 3):
        user_input = input("Pull a lever (y/n): ")
        if user_input == "y" or user_input == "Y":
            return True 
        else:
            return False

    elif tupla == (3, 2):
        user_input = input("Pull a lever (y/n): ")
        if user_input == "y" or user_input == "Y":
            return True 
        else:
            return False
    else:
        return False

def play_one_move(col, row, valid_directions, coins):
    ''' Plays one move of the game
        Return if victory has been obtained and updated col,row '''
    victory = False
    direction = input("Direction: ")
    direction = direction.lower()

    if not direction in valid_directions:
        print("Not a valid direction!")
    else:
        col, row = move(direction, col, row)
        lever_a = lever(col, row)
        if lever_a: 
            coins += 1
            print("You received 1 coin, your total is now", str(coins) +".")
        victory = is_victory(col, row)
    return victory, col, row, lever, coins

# The main program starts here
victory = False
row = 1
col = 1
coins = 0

valid_directions = NORTH
print_directions(valid_directions)

while not victory:
    victory, col, row, lever_a, coins = play_one_move(col, row, valid_directions, coins)
    if victory:
        print("Victory! Total coins", str(coins) + ".")
    else:
        valid_directions = find_directions(col, row)
        print_directions(valid_directions)