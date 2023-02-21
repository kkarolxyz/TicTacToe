import random


class TicTacToe:

    def __init__(self) -> None:
        self.board = []

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
        self.board.append(row)

    def get_random_first_player(self):
        pass

    def fix_spot(self, row, col, player):
        self.board[row][col] = player

    def player_won(self,player):
        n = len(self.board)
        board_values = set()

        # check rows
        for i in range(n):
           for j in range(n):
               board_values.add(self.board[i][j])

           if board_values == {player}:
               return True
           else:
               board_values.clear()

        # check cols
        for i in range(n):
           for j in range(n):
               board_values.add(self.board[j][i])

           if board_values == {player}:
               return True
           else:
               board_values.clear()
        

        


t = TicTacToe()
t.create_board()
