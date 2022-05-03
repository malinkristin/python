class Game:
    def __init__(self):
        self.moves_count = 0
        self.active_player = "X"

    def play(self):
        game_over = False
        max_moves = 9

        while not game_over and self.moves_count != max_moves:
            self.print_board()
            print("It's Player " + self.active_player + "'s turn.")

            taken = True
            while taken:
                value = input("Choose a field.")
                chosen = int(value)
                if not self.is_taken(chosen):
                    taken = False
                    self.squares[chosen - 1] = self.active_player
                    self.moves_count += 1

            game_over = self.check_winner()
            if game_over:
                self.print_board()
                print("Player " + self.active_player + " has won the game.")
                return

            if self.moves_count == max_moves:
                self.print_board()
                print("Draw.")
                return

            self.switch_active_player()

    def switch_active_player(self):
        if self.active_player == 'X':
            self.active_player = 'O'
        else:
            self.active_player = 'X'

    # Board
    squares = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    def print_board(self):
        print("[" + self.squares[0] + "] [" + self.squares[1] + "] [" + self.squares[2] + "]")
        print("[" + self.squares[3] + "] [" + self.squares[4] + "] [" + self.squares[5] + "]")
        print("[" + self.squares[6] + "] [" + self.squares[7] + "] [" + self.squares[8] + "]")

    def check_winner(self):
        return self.squares[0] == 'X' and self.squares[1] == 'X' and self.squares[2] == 'X' \
               or self.squares[3] == 'X' and self.squares[4] == 'X' and self.squares[5] == 'X' \
               or self.squares[6] == 'X' and self.squares[7] == 'X' and self.squares[8] == 'X' \
               or self.squares[0] == 'X' and self.squares[3] == 'X' and self.squares[6] == 'X' \
               or self.squares[1] == 'X' and self.squares[4] == 'X' and self.squares[7] == 'X' \
               or self.squares[2] == 'X' and self.squares[5] == 'X' and self.squares[8] == 'X' \
               or self.squares[0] == 'X' and self.squares[4] == 'X' and self.squares[8] == 'X' \
               or self.squares[2] == 'X' and self.squares[4] == 'X' and self.squares[6] == 'X' \
               or self.squares[0] == 'O' and self.squares[1] == 'O' and self.squares[2] == 'O' \
               or self.squares[3] == 'O' and self.squares[4] == 'O' and self.squares[5] == 'O' \
               or self.squares[6] == 'O' and self.squares[7] == 'O' and self.squares[8] == 'O' \
               or self.squares[0] == 'O' and self.squares[3] == 'O' and self.squares[6] == 'O' \
               or self.squares[1] == 'O' and self.squares[4] == 'O' and self.squares[7] == 'O' \
               or self.squares[2] == 'O' and self.squares[5] == 'O' and self.squares[8] == 'O' \
               or self.squares[0] == 'O' and self.squares[4] == 'O' and self.squares[8] == 'O' \
               or self.squares[2] == 'O' and self.squares[4] == 'O' and self.squares[6] == 'O'

    def is_taken(self, square):
        if self.squares[square - 1] == "X" or self.squares[square - 1] == "O":
            print("This one's taken. Choose another square.")
            return True
        else:
            return False


# start the game
tictactoe = Game()
tictactoe.play()
