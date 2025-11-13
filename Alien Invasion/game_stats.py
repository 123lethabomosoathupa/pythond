class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()  # Set stats to their starting values

        # High score is tracked across games (not reset when starting a new one)
        self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        # Number of ships (lives) the player has left
        self.ships_left = self.settings.ship_limit  
        # Player's current score
        self.score = 0  
        # Current level (starts at 1, increases after clearing waves)
        self.level = 1  
