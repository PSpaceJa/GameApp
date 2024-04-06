"""
Ugwu, K. K. (2023, July 15). Python tutorial for creating a coin-flip simulation. DEV Community. https://dev.to/kelechikizito/python-tutorial-for-creating-a-coin-flip-simulation-56aa#:~:text=1%20Overview%20of%20a%20coin-flip%20simulation%202%20Using,techniques%20Recommendations%20for%20other%20techniques%205%20Conclusion%20Conclusion
python coding for coin toss with step by step explanation in comments - Search Videos. (n.d.). https://www.bing.com/videos/riverview/relatedvideo?&q=python+coding+for+coin+toss+with+step+by+step+explanation+in+comments&&mid=B89A5C4A18DA0EDADCA6B89A5C4A18DA0EDADCA6&mmscn=mtsc&aps=89&FORM=VRDGAR
"""
import random
# Importing the random module for generating random numbers
import statistics


# Importing the statistics module for descriptive analytics

class CoinTossGame:
    average_score = 0  # Initialize average score
    total_score = 0  # Initialize total score
    total_games = 0  # Initialize total number of games played
    show_info = False
    """
    Coin Toss Game: Simulates a coin being tossed where the user guesses heads or tails.

    Attributes:
        score (int): Stores the user's score.
    """

    def __init__(self):
        """
        Initializes the CoinTossGame object with a score of 0.
        """
        self.score = 0

    def play(self):
        """
        Allows the user to play.
        """
        try:
            while True:
                print(self.total_games)
                self.total_games += 1
                input("Press Enter to toss the coin: ")
                # Prompt the user to toss the coin
                result = random.choice(["Heads", "Tails"])
                # Randomly choose "Heads" or "Tails"

                guess = input("Guess the outcome (Heads/Tails): ").capitalize()
                # Prompt user to guess
                if guess == result:
                    print("Fantastic! You are correct!")
                    self.score += 10
                    # Increment score if guessed correctly
                else:
                    print("Incorrect!, Good Try!")
                print(f"Your current score: {self.score}")
                # Display the user's current score
                play_again = input("Do you want to play again? (yes/no): ").lower()
                while play_again != "yes" and play_again != "no":
                    print("Please enter yes or no.")
                    play_again = input("Do you want to play again? (yes/no): ").lower()
                    if play_again == "yes" or play_again == "no":
                        break
                if play_again == "yes":
                    continue
                else:
                    break
        except KeyboardInterrupt:
            print("\nExiting Coin Toss game.")

    def coin_toss_manager(self):
        """
        Main function to run the coin toss game.
        """
        coin_toss_game = CoinTossGame()  # Create an instance of CoinTossGame
        try:
            while True:
                print(self.total_games)
                coin_toss_game.play()  # Play the coin toss game
                coin_toss_game.total_games = self.total_games
                self.total_score += coin_toss_game.score  # Update total score
                self.total_games += 1  # Increment total games played
                print(f"\nTotal games played: {self.total_games}")
                print(f"Total score: {self.total_score}")
                # print(f"Average score: {average_score}")
                play_again = input("Do you want to play another round of Coin Toss? (yes/no): ").lower()
                if play_again != "yes":
                    self.average_score = self.total_score / self.total_games  # Calculate average score
                    print("Exiting the game. Goodbye!")
                    show_info = True
                    break
                else:
                    show_info = False
                    coin_toss_game.score += self.total_score  # Accumulate scores
        except KeyboardInterrupt:
            print("\nExiting the game. Goodbye!")
