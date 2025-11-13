import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """A class to manage the player's ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect (bounding box).
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store the ship's horizontal position as a float for smooth movement.
        # (rect.x only supports integers, so we track x separately).
        self.x = float(self.rect.x)

        # Movement flags; determine if the ship should move left/right.
        self.moving_right = False
        self.moving_left = False

    def center_ship(self):
        """Re-center the ship at the bottom of the screen (after losing a life)."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def update(self):
        """Update the ship's position based on movement flags."""
        # Move right if flag is set and ship is not at the right edge.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        # Move left if flag is set and ship is not at the left edge.
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x (convert float back to int).
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
