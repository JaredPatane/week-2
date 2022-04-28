
#Name: Jared Patane
#Assingment: tic-tac-toe
def display_grid(grid):
    print(f"{grid[0]}|{grid[1]}|{grid[2]}")
    print("-+-+-")
    print(f"{grid[3]}|{grid[4]}|{grid[5]}")
    print("-+-+-")
    print(f"{grid[6]}|{grid[7]}|{grid[8]}")
def next_player(player):
    if player == "o" or player == "":
        return "x"
    elif player == "x":
        return "o"
def player_turn(turn,grid):
    square = int(input(f"{turn}'s turn to choose a square (1-9): "))
    grid[square - 1] = turn
def win_condition(grid):
    return (grid[0] == grid[1] == grid[2] or
    grid[3] == grid[4] == grid[5] or
    grid[6] == grid[7] == grid[8] or
    grid[0] == grid[3] == grid[6] or
    grid[1] == grid[4] == grid[7] or
    grid[2] == grid[5] == grid[8] or
    grid[0] == grid[4] == grid[8] or
    grid[2] == grid[4] == grid[6])
def draw_condition(grid):
    for i in range(9):
        if grid[i] != "x" and grid[i] != "o":
            return False
    return True
def main():
    grid = [1,2,3,4,5,6,7,8,9] 
    player = next_player("")
    while not win_condition(grid) or draw_condition(grid):
        display_grid(grid)
        player_turn(player, grid)
        player = next_player(player)
    display_grid(grid)
    print("Good game. Thanks for playing!")
    pass
if __name__=="__main__":
    main()