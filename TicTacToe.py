# User. (2023, January 19). What constitutes the end of a Tic Tac Toe game? [Closed question]. BoardGames Stack Exchange. https://boardgames.stackexchange.com/questions/58437/what-constitutes-the-end-of-a-tic-tac-toe-game

import statistics


def calculate_stats(data):
    mean = sum(data) / len(data)
    median = statistics.median(data)
    mode = statistics.mode(data)
    return mean, median, mode


def display_board():
    for i in range(0, 9, 3):
        print(f"{TicTacToe.board[i]} | {TicTacToe.board[i + 1]} | {TicTacToe.board[i + 2]}")
        if i < 6:
            print("---------")


def check_win(player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if TicTacToe.board[condition[0]] == TicTacToe.board[condition[1]] == TicTacToe.board[condition[2]] == player:
            return True
    return False


class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9
        self.show_info = False
        self.player1_name = ""
        self.player2_name = ""
        self.player1_wins = 0
        self.player2_wins = 0
        self.rounds = 0

    def display_board(self):
        for i in range(0, 9, 3):
            print(f"{self.board[i]} | {self.board[i + 1]} | {self.board[i + 2]}")
            if i < 6:
                print("---------")

    def check_win(self, player):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] == player:
                return True
        return False

    def play_game(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.rounds += 1

        current_player = 'X'
        while True:
            self.display_board()
            position = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1

            if self.board[position] == ' ':
                self.board[position] = current_player
                if self.check_win(current_player):
                    self.display_board()
                    if current_player == 'X':
                        self.player1_wins += 1
                        print(f"{player1_name} wins!")
                    else:
                        self.player2_wins += 1
                        print(f"{player2_name} wins!")
                    break
                elif ' ' not in self.board:
                    self.display_board()
                    print("It's a draw!")
                    break
                else:
                    current_player = 'O' if current_player == 'X' else 'X'
            else:
                print("That position is already taken. Try again.")

        print(f"{player1_name}'s score: {self.player1_wins}")
        print(f"{player2_name}'s score: {self.player2_wins}")

        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again == 'yes':
            self.play_game(self.player1_name, self.player2_name)
            self.show_info = False
        elif play_again == 'no':
            self.show_info = True