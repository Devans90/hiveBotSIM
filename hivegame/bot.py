class HiveBot:
    def __init__(self, strategy):
        self.strategy = strategy
        self.game_state = None
        self.turn_number = 0

    def update_game_state(self, new_state):
        self.game_state = new_state
        self.turn_number += 1

    def make_move(self):
        move = self.strategy.decide_move(self.game_state)
        return move

class BotStrategyInterface:
    def decide_move(self, game_state):
        raise NotImplementedError

class AggressiveStrategy(BotStrategyInterface):
    def decide_move(self, game_state):
        # Implement aggressive move logic
        pass

class DefensiveStrategy(BotStrategyInterface):
    def decide_move(self, game_state):
        # Implement defensive move logic
        pass

# Creating a bot with a specific strategy
aggressive_bot = HiveBot(AggressiveStrategy())
defensive_bot = HiveBot(DefensiveStrategy())
