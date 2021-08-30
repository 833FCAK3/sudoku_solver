import functions as f

# Initialize the start game grid
# Currently unsolvable grid from API
# grid = [[5, 4, 0, 0, 0, 0, 2, 0, 0, ],
#         [0, 0, 0, 0, 3, 8, 0, 0, 0, ],
#         [0, 6, 0, 0, 0, 0, 0, 0, 4, ],
#         [0, 0, 0, 9, 0, 1, 7, 0, 0, ],
#         [0, 0, 7, 0, 0, 0, 4, 0, 0, ],
#         [0, 0, 5, 0, 0, 0, 0, 1, 0, ],
#         [0, 0, 0, 7, 0, 0, 0, 4, 0, ],
#         [4, 0, 1, 0, 5, 0, 0, 0, 0, ],
# [0, 0, 0, 2, 0, 0, 0, 5, 0]]
# Hard grid solved without guesses
# grid = [[9, 2, 0, 4, 5, 6, 0, 0, 3],
#         [0, 3, 0, 0, 0, 0, 0, 0, 0],
#         [0, 1, 4, 0, 7, 0, 0, 0, 9],
#         [0, 0, 7, 0, 0, 5, 3, 0, 0],
#         [8, 0, 0, 0, 0, 2, 0, 7, 0],
#         [4, 0, 0, 1, 0, 0, 9, 0, 8],
#         [0, 0, 0, 6, 0, 3, 0, 0, 0],
#         [0, 4, 1, 0, 0, 0, 0, 0, 7],
#         [3, 0, 0, 0, 0, 4, 5, 6, 1]]
# Another Truly Hard grid 1 guess
# grid = [[0, 0, 0, 0, 0, 0, 6, 8, 7],
#         [0, 0, 0, 0, 0, 0, 9, 0, 0],
#         [0, 0, 0, 6, 0, 8, 0, 5, 0],
#         [0, 0, 0, 0, 0, 0, 0, 6, 0],
#         [0, 8, 5, 1, 2, 0, 0, 0, 9],
#         [2, 1, 0, 0, 4, 6, 0, 0, 0],
#         [4, 7, 3, 0, 0, 0, 0, 0, 1],
#         [8, 0, 0, 0, 9, 0, 0, 0, 0],
#         [0, 2, 0, 0, 0, 7, 0, 0, 0]]
# Truly Hard grid 7 guesses
grid = [[6, 4, 0, 2, 0, 0, 3, 0, 0],
        [0, 0, 0, 9, 8, 0, 0, 0, 0],
        [0, 0, 7, 0, 1, 0, 0, 0, 0],
        [0, 0, 2, 3, 0, 0, 0, 0, 5],
        [0, 0, 4, 5, 6, 0, 0, 0, 0],
        [1, 0, 5, 0, 0, 9, 6, 7, 0],
        [0, 0, 6, 0, 0, 0, 5, 1, 7],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [7, 5, 3, 0, 0, 0, 0, 0, 4]]
# Expert grid
# grid = [[0, 0, 0, 0, 0, 0, 0, 9, 0],
#         [0, 9, 7, 0, 0, 0, 4, 0, 0],
#         [0, 0, 8, 0, 6, 0, 0, 7, 0],
#         [0, 0, 0, 9, 8, 7, 0, 0, 0],
#         [0, 0, 0, 0, 0, 4, 0, 0, 1],
#         [0, 0, 0, 0, 0, 6, 0, 2, 4],
#         [2, 0, 0, 0, 0, 0, 5, 0, 3],
#         [0, 4, 0, 0, 5, 0, 0, 0, 0],
#         [6, 0, 0, 8, 0, 0, 0, 0, 0]]

# Pass one of the above grids to the function to test specific ones, or leave empty to solve a random grid.
grid = f.main()
