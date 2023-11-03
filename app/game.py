import math

class TicTacToe():
    def __init__(self):
        self.board = [' ' for space in range(9)]
        self.winner = None
    
    def main_menu(self):
        val = int(input('1. Play vs person\n2. Play vs AI\n3. Quit\n'))
        if val < 1 or val > 3:
            val = int(input('\nInvalid choice! please pick a number from 1 to 3.\n\n1. Play vs person\n2. Play vs AI\n3. Quit\n'))
        return val

if __name__ == "__main__":
    game = TicTacToe()
    val = game.main_menu()