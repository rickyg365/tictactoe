import os
import sys

"""
Program: Tic Tac Toe
Author: rickyg3
Date: 09/01/21
"""


# Functions
def clear_screen():
    clear_command = "clear"

    if sys.platform == "win32":
        clear_command = "cls"

    os.system(clear_command)


# Classes
class TicTacToe:
    def __init__(self):
        self.round = 0

        self.o_moves = []
        self.x_moves = []

        self.data = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]

        self.in_use = []

        self.turn = 0

        self.o_score = 0
        self.x_score = 0

        self.display = str(self)

    def __str__(self):
        """
        Score: [O]: 0 | [X]: 0

        """
        text = f"Score: \n O: {self.o_score}     X: {self.x_score}\n"

        # Variables
        uni_column = '\u2503'
        uni_row = '\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u254B\u2501\u2501\u2501'

        for _, row in enumerate(self.data):
            text += f"\n{row[0]:^3}{uni_column}{row[1]:^3}{uni_column}{row[2]:^3}"
            if _ != 2:
                text += f"\n{uni_row}"

        text += '\n'

        return text

    def reset(self):
        self.round = 0

        self.o_moves = []
        self.x_moves = []

        self.in_use = []

        self.data = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]

        self.update_display()

    @staticmethod
    def intro_screen():
        intro = f"""Score:
 O: (o-score)     X: (x-score)

 1 ┃ 2 ┃ 3  
━━━╋━━━╋━━━ 
 4 ┃ 5 ┃ 6  
━━━╋━━━╋━━━ 
 7 ┃ 8 ┃ 9    

Choose spot [ current-player ]: (input-number)
"""
        print(intro)
        input("Press Enter to continue...")

    def switch_turns(self):
        self.round += 1
        if self.turn < 1:
            self.turn += 1
            return
        self.turn -= 1

    def current_symbol(self):
        player_turn = {
            0: 'O',
            1: 'X'
        }

        return player_turn.get(self.turn)

    def append_player_move(self, data):
        if self.turn == 0:
            self.o_moves.append(data)
            return

        self.x_moves.append(data)
        return

    def make_move(self, tup):
        # move variables
        player_symbol = self.current_symbol()
        x, y = tup

        self.data[x][y] = player_symbol

        self.append_player_move(tup)

        # It is only up to this point that the round counter goes up after it passes all the previous code
        self.switch_turns()

        return True

    def check_win(self):

        current_turn = f"{'o' if self.turn == 0 else 'x'}"

        for i in range(3):
            new_column = []
            new_row = []
            for j in range(3):
                # Row
                new_row.append(self.data[i][j])
                # Col
                new_column.append(self.data[j][i])

            # Check each row
            if len(new_row) >= 3:
                empty_row_condition = new_row[1] != ' '
                if new_row[0] == new_row[1] and new_row[1] == new_row[2] and empty_row_condition:
                    return True

            # Check each col
            if len(new_column) >= 3:
                empty_col_condition = new_column[1] != ' '
                if new_column[0] == new_column[1] and new_column[1] == new_column[2] and empty_col_condition:
                    return True

        # Diagonal
        diag_empty = self.data[1][1] != ' '
        if self.data[0][0] == self.data[1][1] and self.data[1][1] == self.data[2][2] and diag_empty:
            return True

        if self.data[0][2] == self.data[1][1] and self.data[1][1] == self.data[2][0] and diag_empty:
            return True

        return False

    def validate_input(self, some_input):
        valid_input = [
            '1',
            '2',
            '3',
            '4',
            '5',
            '6',
            '7',
            '8',
            '9'
        ]

        not_valid = some_input not in valid_input
        repeat = some_input in self.in_use

        if not_valid or repeat:
            return False

        self.in_use.append(some_input)
        return True

    def process_input(self, raw_input):
        key_map = {
            '1': (0, 0),
            '2': (0, 1),
            '3': (0, 2),
            '4': (1, 0),
            '5': (1, 1),
            '6': (1, 2),
            '7': (2, 0),
            '8': (2, 1),
            '9': (2, 2)
        }
        return key_map.get(raw_input)

    def update_display(self):
        self.display = str(self)

    def print_display(self):
        self.update_display()
        clear_screen()
        print(self.display)

    def run_match(self):
        """   """
        # Reset Board, just in case
        self.reset()

        # Main Game loop
        while True:
            # if more than 9 rounds end game, because board is full
            if self.round == 9:
                self.reset()
                print("\nTied Game!")
                return True

            # display board
            self.print_display()

            # User input
            try:
                user_input = input(f"Choose spot [{'O' if self.turn == 0 else 'X'}]: ")

                valid_input = self.validate_input(user_input)
                if not valid_input:
                    input("Invalid Input, try again sucker.")
                    continue

                cleaned_input = self.process_input(user_input)

                self.make_move(cleaned_input)  # Honestly even if it returns false nothing happens

            except KeyboardInterrupt:
                print("\n \n[Program Closed]: Match interrupted\n")
                return False

            # Check for win
            win_status = self.check_win()

            # for a win
            if win_status:
                x_win = self.turn == 0

                if x_win:
                    self.x_score += 1
                    self.print_display()
                    print('X Wins!')
                    return True

                self.o_score += 1
                self.print_display()
                print('O Wins!')

                # self.reset()

                return True

    def run_game(self):
        clear_screen()
        self.intro_screen()

        try:
            while True:
                successful_match = self.run_match()

                if not successful_match:
                    break

                play = input("\nPlay again?: ")

                exit_options = [
                    'q',
                    'n'
                ]
                play_status = False if play in exit_options else True

                if not play_status:
                    break

        except KeyboardInterrupt:
            print("\n \n[Program Closed]\n")


if __name__ == "__main__":
    new_game = TicTacToe()

    new_game.run_game()
