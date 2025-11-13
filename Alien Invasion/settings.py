class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings (don't change mid-game)."""
        # Screen settings
        self.screen_width = 1200      # Window width
        self.screen_height = 800      # Window height
        self.bg_color = (230, 230, 230)  # Background color (light gray)

        # Ship settings
        self.ship_limit = 3  # Number of lives/ships the player starts with

        # Bullet settings
        self.bullet_width = 3          # Bullet thickness
        self.bullet_height = 15        # Bullet length
        self.bullet_color = (60, 60, 60)  # Dark gray bullet
        self.bullets_allowed = 3       # Max bullets on screen at once

        # Alien settings
        self.fleet_drop_speed = 10  # How far the fleet drops when hitting an edge

        # Game difficulty scaling factors
        self.speedup_scale = 1.1   # Speed increases by 10% after each wave
        self.score_scale = 1.5     # Points per alien increase by 50% after each wave

        # Initialize settings that change throughout the game
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change as the game progresses."""
        # Initial movement speeds
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0

        # Fleet direction: 1 = move right, -1 = move left
        self.fleet_direction = 1

        # Initial scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values after each wave."""
        # Make ships, bullets, and aliens move faster
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        # Increase score value of aliens
        self.alien_points = int(self.alien_points * self.score_scale)
