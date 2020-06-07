##
## Import and initialize the librarys
import pygame
from item_storage import *
from pygame_ess import pygame_ess


##
## Initialization
pygame.init()

# Set up the drawing window
window_size = (1024, 768)
screen = pygame.display.set_mode((1024, 768))
window = pygame.surface.Surface((window_size))


##
## Variables
page_name = 'monoalphabetic_cipher'
button_types = {'back':'back', 'info':''}
monoalphabetic_cipher_screen = dict()


##
## Load home screen images

# background image
monoalphabetic_cipher_screen = pygame_ess.load_images([page_name])

# Buttons
for button_type in button_types.keys():
    monoalphabetic_cipher_screen[button_type] = item(button_type,
                                      pygame_ess.load_images([page_name, button_type]),
                                      coord(47 + 766 * list(button_types.keys()).index(button_type), 28, 
                                            162, 67, 
                                            (48 + 766) * list(button_types.keys()).index(button_type), 0))


##
## 
class monoalphabetic_cipher:

    def algorithm(plaintext, key):
        pass

    def load_monoalphabetic_cipher():
        screen.blit(monoalphabetic_cipher_screen['background'], (0,0))
        
        pygame_ess.update()
    
    def run():
        # Load screen
        monoalphabetic_cipher.load_monoalphabetic_cipher()
        
        # Check for selection
        while True:
            selection_result = pygame_ess.selection(screen, monoalphabetic_cipher_screen, button_types)
            if selection_result == True: monoalphabetic_cipher.load_monoalphabetic_cipher()
            elif selection_result == 'back': break

            if pygame_ess.buffer(): break