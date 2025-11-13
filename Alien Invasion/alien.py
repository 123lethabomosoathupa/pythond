import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()  
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and get its rectangle (position & size).
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top-left corner of the screen.
        # Position is set to one alien width & height away from edges.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position (as a float).
        # This allows smoother movement compared to using only integers.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at the edge of the screen."""
        screen_rect = self.screen.get_rect()
        # If the alien touches the left or right edge, return True.
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        """Move the alien right or left depending on fleet direction."""
        # Move alien horizontally based on speed and fleet direction.
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x  # Update rect position from float
