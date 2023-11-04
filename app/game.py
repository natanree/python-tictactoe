import math

class TicTacToe():
    def __init__(self):
        self.board = [[' ' for column in range(3)] for row in range(3)]
        self.winner = None
    
    def display_board_guide(self):
        print('| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |\n')

    def display_board(self):
        for row in self.board:
            print('| ' + ' | '.join(row) + ' |')

    def get_board_input(self):
        self.display_board()
        val = int(input('\nInput Choice: '))
        if val < 1 or val > 3:
            val = int(input('\nInvalid choice! please pick a number from 1 to 9: '))
        return val 

    def main_menu(self):
        val = int(input('1. Play vs person\n2. Play vs AI\n3. Quit\n'))
        if val < 1 or val > 3:
            val = int(input('\nInvalid choice! please pick a number from 1 to 3.\n\n1. Play vs person\n2. Play vs AI\n3. Quit\n'))
        return val

if __name__ == "__main__":
    game = TicTacToe()
    val = game.get_board_input()