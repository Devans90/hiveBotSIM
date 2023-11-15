from hivegame import *
from hivegame.hive import Hive  # Importing the Hive class
from hivegame.bot import *  # Importing the Bot

class HiveGameManager:
    def __init__(self, bot1, bot2):
        self.hive = Hive()  # Instance of the Hive class
        self.bot1 = bot1
        self.bot2 = bot2
        self.hive.setup()  # Setup the game

    def play(self):
        # Main game loop
        while self.hive.check_victory() == Hive.UNFINISHED:
            current_bot = self.bot1 if self.hive.activePlayer == 0 else self.bot2
            move = current_bot.make_move()
            
            # Execute the move using the Hive class's action method
            try:
                self.hive.action('play', move)
            except Exception as e:
                # Handle illegal move or other exceptions
                print(f"Illegal move or error: {e}")
                continue  # Optionally, you can have more sophisticated handling here

            # Switch turns
            self.hive.activePlayer = 1 - self.hive.activePlayer

# Creating and using the game manager
# bot1 and bot2 are instances of your bot class, initialized with different strategies

bot1 =  HiveBot(AggressiveStrategy())
bot2 =  HiveBot(DefensiveStrategy())

game_manager = HiveGameManager(bot1, bot2)
game_manager.play()
