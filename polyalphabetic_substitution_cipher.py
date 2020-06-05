##
## Import and initialize the librarys
import pygame
from image_storage import *
from pygame_ess import pygame_ess


##
## Initialization
pygame.init()

# Set up the drawing window
window_size = (1024, 768)
screen = pygame.display.set_mode((1024, 768))
window = pygame.surface.Surface((window_size))


##
## 
class polyalphabetic_substitution_cipher:
    def run():        
        while True:
            if pygame_ess.buffer(): break