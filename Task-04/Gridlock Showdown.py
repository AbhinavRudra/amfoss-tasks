'''
Help Mike, Hawk and Selena have great fun at a park
Selena proposed a game where the park is divided into a 3x3 grid,
where the three of them take turns to claim a spot of their choice each time. The first person to obtain 3 spots aligned diagonally,
vertically or horizontally to each other wins. There can only be one victor and in the event that none of them obtain three aligned spots, 
it is considered a draw.'''
def check_game_result(grid):

    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2] and grid[i][0] != '.':
            return grid[i][0]
        if grid[0][i] == grid[1][i] == grid[2][i] and grid[0][i] != '.':
            return grid[0][i]
    
    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != '.':
        return grid[0][0]
    if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != '.':
        return grid[0][2]
    
    return "DRAW"


def main():
    t = int(input())
    for _ in range(t):
        grid = [list(input().strip()) for _ in range(3)]
        result = check_game_result(grid)
        print(result)

if __name__ == "__main__":
    main()