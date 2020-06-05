##
## Import and initialize the librarys
import pygame
from pygame_ess import pygame_ess
from image_storage import *
from caesar_cipher import caesar_cipher


##
## Initialization
pygame.init()

# Set up the drawing window
window_size = (1024, 768)
screen = pygame.display.set_mode((1024, 768))
window = pygame.surface.Surface((window_size))
pygame.display.set_caption("Cryptography")


##
## Variables
image_dir = 'images/cryptography/'

cipher_types = {'caesar_cipher':caesar_cipher, 'monoalphabetic_cipher':'', 'homophonic_substitution_cipher':'',
                'polygram_subsitution_cipher':'', 'polyalphabetic_substitution_cipher':''}

home_screen = dict()


##
## Load home screen images

# background image
home_screen['background'] = pygame_ess.load_images(image_dir)

# cipher list
for cipher_type in cipher_types.keys():
    cipher_type_y_coord = 112 + list(cipher_types.keys()).index(cipher_type) * 106
    home_screen[cipher_type] = image_item(cipher_type,
                                      pygame_ess.load_images(image_dir+cipher_type+'/'),
                                      coord(47, cipher_type_y_coord, 929, 86, 0, cipher_type_y_coord))


##
## Key home screen functions
def load_home_screen():
    # Load background
    screen.blit(home_screen['background']['cryptography_bg'], (0,0))

    # Load each option
    for cipher_type in cipher_types.keys():
        screen.blit(home_screen[cipher_type].images['button'], (home_screen[cipher_type].button.image_coord()))
        
    pygame_ess.update()
    

##
## Main loop
load_home_screen()

while True:
    # Check for selection
    #selection()
    if pygame_ess.selection(screen, home_screen, cipher_types):
        load_home_screen()
    
    # End program
    if pygame_ess.buffer(): break

# Done! Time to quit.
pygame.quit()
