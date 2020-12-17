class Cell:
    def __init__(self, value=None):
        self.value = value
        self.preset = False if value is None else True
        self.temp = []

        
class Board:
    def __init__(self, matrix):
        self.board = []

    def __getitem__(self, key):
        return self.board[key]

    def __setitem__(self, key, value):
        # make sure user cannot set preset values
        self.board[key] = value