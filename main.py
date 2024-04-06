from CoinTossGame import CoinTossGame
from DiceRollGame import DiceRollGame
from TicTacToe import TicTacToe
from WordJumbleGame import WordJumbleGame

def main():
    while True:
        print("\nWelcome to the Game Center!")
        print("1. Coin Toss")
        print("2. Dice Roll")
        print("3. Tic Tac Toe")
        print("4. Word Jumble")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            coin_game = CoinTossGame()
            coin_game.coin_toss_manager()
        elif choice == '2':
            dice_game = DiceRollGame()
            dice_game.die_game_manager()
        elif choice == '3':
            tic_tac_toe_game = TicTacToe()
            player1_name = input("Enter Player 1's name: ")
            player2_name = input("Enter Player 2's name: ")
            tic_tac_toe_game.play_game(player1_name, player2_name)
        elif choice == '4':
            word_jumble_game = WordJumbleGame()
            word_jumble_game.play_game()
        elif choice == '5':
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()