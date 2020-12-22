board_med = [[[], [], [], 9, [], 7,  [], 3, []],
             [[], [], 8,  4, [], 3,  [], [], []],
             [[], [], 7,  [], 2, [], [], 5, 4],
             [9, 7, [], 3, 4, 1, 5, 8, []],
             [5, 8, [], 7, [], 6, [], [], 2],
             [6, 3, [], 2, 8, 5, [], 9, 1],
             [[], 1, 5, [], [], [], [], [], []],
             [[], [], [], 6, [], [], [], 2, []],
             [[], [], [], 5, 7, [], [], [], []],
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

class Grid:
    def __init__(self, x, y, matrix, GRID_SIZE=3):
        self.grid = [board_med[i][x:x+GRID_SIZE] for i in range(y, y+GRID_SIZE)]
        self._missing = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def __repr__(self):
        output = ""
        for row in self.grid:
            output += f"{row}\n"
        return output

    @property
    def missing(self):
        for row in self.grid:
            for value in row:
                try:
                    self._missing.remove(value)
                except ValueError:
                    pass
        return self._missing


class Board:
    def __init__(self, matrix, SIZE=9, GRID_SIZE=3):
        self.SIZE = SIZE
        self.GRID_SIZE = GRID_SIZE

        self.board = matrix
        self._grids = dict()

    @property
    def grids(self):
        for y in range(0, self.SIZE-self.GRID_SIZE+1, self.GRID_SIZE):
            for x in range(0, self.SIZE-self.GRID_SIZE+1, self.GRID_SIZE):
                self._grids[x, y] = Grid(x, y, self.board)
        return self._grids

    def __getitem__(self, key):
        return self.board[key]

    def row(self, x):
        return self.board[x]
    
    def col(self, y):
        output = []
        for row in self.board:
            output.append(row[y])
        return output

    def __repr__(self):
        output = ""
        for row in self.board:
            output += f"{row}\n"
        return output        
b = Board(board_med)
# print(b.grids[0,0].missing)
# print(b[0][3])
# print(b.temps)

# values = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def pre_process(b):
    for x, row in enumerate(b.board):
        for y, cell in enumerate(row):
            if cell == []:
                print(x, y)
                print(f"Grid:\n{b.grids[3*(y//3),3*(x//3)]}")
                temp = b.grids[3*(y//3),3*(x//3)].missing
                print(f"missing: {temp}")
                print(f"row: {b.row(y)}")
                print(f"col: {b.col(x)}")
                for val in b.row(y):
                    if val in temp:
                        temp.remove(val)
                for val in b.col(x):
                    if val in temp:
                        temp.remove(val)
                print(f"temp: {temp}")
                b.board[x][y] = temp

# b.board[x][y] = temp[0] if len(temp) == 1 else temp
pre_process(b)
print(b)
# for x, row in enumerate(b.board):
#     for y, cell in enumerate(row):
#         if type(cell) == list and len(cell) == 1:
#             b.board[x][y] = cell[0]
#             pre_process(b)
# print(b.grids.keys())
# print([grid.missing for grid in b.grids.values()])