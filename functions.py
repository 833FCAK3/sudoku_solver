import numpy as np
import requests


# Initialize viriables
possibilities = [i for i in range(1, 10)]
grid_copy_list = []
option_number = 0
reset_done = False


def main(grid=None):
    """Loop through the grid and check if the tile is subject to change and is 'locked in' either by value or grid exclusion method, fill it in if so
    If the grid is not solvable by exlusions alone, start making 'guesses', that is for tiles that have only two possible values left choose the first one and try to solve the grid again, make another guess if the situation repeats itself. Has dead end check that reverts the grid state to that prior the guess and chooses alternative possibility. Can make and recover from up to 2 wrong guesses, assuming it detects the dead end immediately after the second wrong one.
    Runs until the grid is solved, returns solved grid upon completion."""
    grid = grid_init(grid)
    grid0 = grid.copy()
    global changes_made, option_number, reset_done
    while not grid_solved(grid):
        changes_made = True
        while changes_made:
            changes_made = False
            for i in range(len(grid.T[0])):
                for u in range(len(grid[0])):
                    if grid[i][u] == 0:
                        pos_left = possibilities.copy()
                        value_grid_exclusion_apply(grid, i, u, pos_left)
                        if len(pos_left) == 0:
                            grid = dead_end_check()
                            break
                else:
                    continue
                break
        guess(grid)
    print_result(grid, grid0)
    return(grid)


def guess(grid):
    """If the grid is not solvable by exlusions alone, start making "guesses", that is for tiles that have only two possible values left choose the first one and try to solve the grid again, make another guess if the situation repeats itself."""
    global option_number, reset_done
    counter1 = 0
    if not grid_solved(grid):
        for i in range(len(grid.T[0])):
            for u in range(len(grid[0])):
                counter1 += 1
                if grid[i][u] == 0:
                    pos_left = possibilities.copy()
                    exclude_values(grid, i, u, pos_left)
                    if 0 < len(pos_left) <= 2:
                        grid_copy_list.append(grid.copy())
                        grid[i][u] = pos_left[option_number]
                        # print(str((i, u)) + ' set to ' +
                        #       str(pos_left[option_number]))
                        if reset_done:
                            option_number = 0
                            reset_done = False
                        break

            else:
                continue
            break


def dead_end_check():
    """In case grid is no longer solvable, restores grid to state prior to last known wrong guess and makes sure different one will be made."""
    global reset_done, option_number, changes_made
    if option_number == 1:
        grid_copy_list.pop()
        reset_done = True
    else:
        option_number = 1
    changes_made = False
    return(grid_copy_list.pop())


def value_grid_exclusion_apply(grid, i, u, pos_left):
    """Excludes horiz, vert and quardant possiblities, if only one left, assigns
    it to the tile, if more - checks if each of those possibilities can be
    present in any of the free tiles in quadrant."""
    exclude_values(grid, i, u, pos_left)
    apply_changes(grid, i, u, pos_left)
    grid_exclusion(grid, i, u, pos_left)


def grid_exclusion(grid, i, u, pos_left):
    """Checks if a possiblity can be present in any other free tile, fills it in
    if it cannot be in any other tile."""
    global changes_made
    if len(pos_left) > 1 and grid[i][u] == 0:
        for pos in pos_left:
            for x, y in Q[current_quadrant]:
                if grid[x][y] == 0 and (x, y) != (i, u):
                    if pos not in grid[x] and pos not in grid.T[y]:
                        break
                    else:
                        continue
            else:
                grid[i][u] = pos
                changes_made = True


def apply_changes(grid, i, u, pos_left):
    """Assigns possiblity to a tile if the possibllity is the only one left in   the list, sets flag 'changes_made' to True so that the while loop continues."""
    if len(pos_left) == 1:
        global changes_made
        grid[i][u] = pos_left[0]
        changes_made = True


def exclude_values(grid, i, u, pos_left):
    """Narrows down a list of possibilites for the tile, exluding values in
    horizontal and vertical dimensions, plus the ones already present in
    quadrant the cell belongs to."""
    exclude_horiz(grid, i, pos_left)
    exclude_vert(grid, u, pos_left)
    exlude_quadrant(grid, pos_left, i, u)


def exclude_horiz(grid, i, pos_left):
    """Excludes possible values in horizontal dimension."""
    for p in grid[i]:
        if p in pos_left:
            pos_left.remove(p)


def exclude_vert(grid, u, pos_left):
    """Excludes possible values in vertical dimension."""
    for p1 in grid.T[u]:
        if p1 in pos_left:
            pos_left.remove(p1)


def exlude_quadrant(grid, pos_left, i, u):
    """Exlude numbers in quadrant to which the tile belongs
    from the list of possible values and set the value of variable
    'current_quadrant' to be used later."""
    global current_quadrant
    # Check and store in which quadrant the tile is.
    for q, v in Q.items():
        if (i, u) in v:
            current_quadrant = q
            for x, y in Q[current_quadrant]:
                if grid[x][y] in pos_left:
                    pos_left.remove(grid[x][y])
    return(current_quadrant)


def grid_init(grid):
    """Checks if the grid has been passed as an argument or it has to be
    retrieved via API."""
    if grid == None:
        grid = np.array(init_grid_api())
    elif grid != None:
        grid = np.array(grid)
    return(grid)


def init_grid_api(url="http://www.cs.utep.edu/cheon/ws/sudoku/new/?size=9&level=2"):
    """Acquire the grid via API."""
    no_grid_msg = "\n\nThere is no Sudoku puzzle to solve!\nMake sure either to pass the grid directly to the 'main' function or that the API request is successul."
    try:
        response = requests.get(url)
        grid = np.array([0]*81).reshape(9, 9)
        # print(response.json())
        for cell in response.json()['squares']:
            grid[cell['x']][cell['y']] = cell["value"]
        return(grid)
    except requests.exceptions.HTTPError as errh:
        print(f"{errh} {no_grid_msg}")
        exit()
    except requests.exceptions.ConnectionError as errc:
        print(f"{errc} {no_grid_msg}")
        exit()
    except requests.exceptions.Timeout as errt:
        print(f"{errt} {no_grid_msg}")
        exit()
    except requests.exceptions.RequestException as err:
        print(f"{err} {no_grid_msg}")
        exit()


def grid_solved(grid):
    """Returns true if the grid has no zeros or duplicates, returns None otherwise."""
    for i in range(9):
        if 0 in grid or len(grid[i]) != len(set(grid[i])) or len(grid.T[i]) != len(set(grid.T[i])):
            break
    else:
        return True


def print_result(grid, grid0):
    """Prints the starting and completed grids in neat format."""
    non_empty_cells = 81
    for row in grid0:
        for number in row:
            if number == 0:
                non_empty_cells -= 1
    print('    Initial grid' + '                Solved grid')
    for i in range(len(grid)):
        print(f"{grid0[i]}       {grid[i]}")
    result(grid)
    print(f"The grid initially had {non_empty_cells} cells filled.")


def result(grid):
    """Inform if the grid was solved successfully or something is off."""
    if grid_solved(grid):
        print("\nGrid has been successfully solved!")
    else:
        print('U messed up m8!')


# List of coordinates of tiles, belonging to each quadrant.
Q = {'q1': list(zip(sorted(list(range(0, 3))*3), sorted(list(range(0, 3)))*3)),
     'q2': list(zip(sorted(list(range(3, 6))*3), sorted(list(range(0, 3)))*3)),
     'q3': list(zip(sorted(list(range(6, 9))*3), sorted(list(range(0, 3)))*3)),
     'q4': list(zip(sorted(list(range(0, 3))*3), sorted(list(range(3, 6)))*3)),
     'q5': list(zip(sorted(list(range(3, 6))*3), sorted(list(range(3, 6)))*3)),
     'q6': list(zip(sorted(list(range(6, 9))*3), sorted(list(range(3, 6)))*3)),
     'q7': list(zip(sorted(list(range(0, 3))*3), sorted(list(range(6, 9)))*3)),
     'q8': list(zip(sorted(list(range(3, 6))*3), sorted(list(range(6, 9)))*3)),
     'q9': list(zip(sorted(list(range(6, 9))*3), sorted(list(range(6, 9)))*3))}
