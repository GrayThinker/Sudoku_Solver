board_med = [[None, None, None, 9, None, 7, None, 3, None],
             [None, None, 8, 4, None, 3, None, None, None],
             [None, None, 7, None, 2, None, None, 5, 4],
             [9, 7, None, 3, 4, 1, 5, 8, None],
             [5, 8, None, 7, None, 6, None, None, 2],
             [6, 3, None, 2, 8, 5, None, 9, 1],
             [None, 1, 5, None, None, None, None, None, None],
             [None, None, None, 6, None, None, None, 2, None],
             [None, None, None, 5, 7, None, None, None, None],
             ]

board_med_soln = [[4, 2, 6, 9, 5, 7, 1, 3, 8],
                  [1, 5, 8, 4, 6, 3, 2, 7, 9],
                  [3, 9, 7, 1, 2, 8, 6, 5, 4],
                  [9, 7, 2, 3, 4, 1, 5, 8, 6],
                  [5, 8, 1, 7, 9, 6, 3, 4, 2],
                  [6, 3, 4, 2, 8, 5, 7, 9, 1],
                  [2, 1, 5, 8, 3, 4, 9, 6, 7],
                  [7, 4, 3, 6, 1, 9, 8, 2, 5],
                  [8, 6, 9, 5, 7, 2, 4, 1, 3],
                  ]
index = 0
GRID_SIZE = 3
grid0 = [[board_med[i][index:index+GRID_SIZE]] for i in range(index, index+GRID_SIZE)]
# print(grid0)

class Grid:
    def __init__(self, index, matrix, GRID_SIZE=3):
        self.grid = [board_med[i][index:index+GRID_SIZE] for i in range(index, index+GRID_SIZE)]
        self.missing = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def __repr__(self):
        output = ""
        for row in self.grid:
            output += f"{row}\n"
        return output

    def missing(self):
        check_missing()
        return self.missing

    def check_missing(self):
        for row in self.grid:
            for value in row:
                try:
                    self.missing.remove(value)
                except ValueError:
                    pass

grid0 = Grid(0, board_med)
print(grid0)
grid0.check_missing()
print(grid0.missing)