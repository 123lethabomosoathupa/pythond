import pygame.font


class Button:
    """A class to build buttons for the game."""

    def __init__(self, ai_game, msg):
        """Initialize button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()  # Get screen boundaries

        # Set the dimensions and properties of the button
        self.width, self.height = 200, 50  # Button size
        self.button_color = (0, 135, 0)    # Dark green button background
        self.text_color = (255, 255, 255)  # White text
        self.font = pygame.font.SysFont(None, 48)  # Default font, size 48

        # Build the button's rect object and center it on screen
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The button message (text) is prepared once
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        # Render text into an image: (message, antialias, text color, bg color)
        self.msg_image = self.font.render(
            msg, True, self.text_color, self.button_color
        )
        # Get a rectangle for the text image
        self.msg_image_rect = self.msg_image.get_rect()
        # Center text on the button rectangle
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw blank button and then draw message."""
        # Draw the button rectangle (filled with button_color)
        self.screen.fill(self.button_color, self.rect)
        # Overlay the text image on top
        self.screen.blit(self.msg_image, self.msg_image_rect)
