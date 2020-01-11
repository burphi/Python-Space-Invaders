import pygame
from pygame.sprite import Sprite

class Star():
    """Create the stars drawn on the screen"""

    def __init__(self, ai_settings, screen):
        """Initialize stars"""
        super(Star, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #Load the image of the star
        self.image = pygame.image.load('images/star')
        self.rect = self.image.get_rect()

        # Place the first star
        self.rect.x = self.rect.width * 2
        self.rect.y = self.rect.height * 2

        # Store the exact position of the stars
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the star at its current position"""
        self.screen.blit(self.image, self.rect)