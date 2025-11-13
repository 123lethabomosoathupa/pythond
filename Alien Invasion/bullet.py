import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color  # Bullet color defined in settings

        # Create a rectangle for the bullet with given width/height.
        # Start at (0, 0) and then place it at the ship's midtop.
        self.rect = pygame.Rect(
            0, 0, 
            self.settings.bullet_width, 
            self.settings.bullet_height
        )
        self.rect.midtop = ai_game.ship.rect.midtop  # Position bullet at ship's gun

        # Store the bullet's vertical position as a float
        # (for smoother movement than using integers only).
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""
        # Decrease the y-coordinate (since (0,0) is top-left in pygame).
        self.y -= self.settings.bullet_speed  
        # Update the rect.y so it moves visually.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
