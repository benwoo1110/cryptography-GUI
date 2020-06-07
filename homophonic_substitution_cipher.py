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
page_name = 'homophonic_substitution_cipher'
button_types = {'back':'back', 'info':''}
homophonic_substitution_cipher_screen = dict()


##
## Load home screen images

# background image
homophonic_substitution_cipher_screen = pygame_ess.load_images([page_name])

# Buttons
for button_type in button_types.keys():
    homophonic_substitution_cipher_screen[button_type] = item(button_type,
                                      pygame_ess.load_images([page_name, button_type]),
                                      coord(47 + 766 * list(button_types.keys()).index(button_type), 28, 
                                            162, 67, 
                                            (48 + 766) * list(button_types.keys()).index(button_type), 0))


##
## 
class homophonic_substitution_cipher:

    def algorithm(plaintext, key):
        pass

    def load_homophonic_substitution_cipher():
        screen.blit(homophonic_substitution_cipher_screen['background'], (0,0))
        
        pygame_ess.update()
    
    def run():
        # Load screen
        homophonic_substitution_cipher.load_homophonic_substitution_cipher()
        
        # Check for selection
        while True:
            selection_result = pygame_ess.selection(screen, homophonic_substitution_cipher_screen, button_types)
            if selection_result == True: homophonic_substitution_cipher.load_homophonic_substitution_cipher()
            elif selection_result == 'back': break

            if pygame_ess.buffer(): break