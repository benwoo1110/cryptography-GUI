######################################
# Import and initialize the librarys #
######################################
import pygame
from pygame_ess import pygame_ess
from item_storage import *
from atbash_cipher import atbash_cipher
from affine_cipher import affine_cipher
from caesar_cipher import caesar_cipher
from monoalphabetic_subsitution_cipher import monoalphabetic_subsitution_cipher
from polyalphabetic_substitution_cipher import polyalphabetic_substitution_cipher


##################
# Initialization #
##################
pygame.init()

# Set up the drawing window
window_size = (1024, 768)
screen = pygame.display.set_mode((1024, 768))
window = pygame.surface.Surface((window_size))
pygame.display.set_caption("Cryptography")


########################
# Variables declaration #
########################
page_name = 'cryptography'

cipher_types = {'atbash_cipher':atbash_cipher,
                'affine_cipher':affine_cipher,
                'caesar_cipher':caesar_cipher, 
                'monoalphabetic_subsitution_cipher':monoalphabetic_subsitution_cipher, 
                'polyalphabetic_substitution_cipher':polyalphabetic_substitution_cipher
                }

cryptography_objects = dict()


############################
# Load home screen objects #
############################

# Load essentials images
pygame_ess.load_essential_objects(cryptography_objects, page_name, back=False, info=False)

# cipher types view list
for cipher_type in cipher_types.keys():
    cipher_type_y_coord = 112 + list(cipher_types.keys()).index(cipher_type) * 106
    cryptography_objects[cipher_type] = item(name=cipher_type,
                                             type='button',
                                             images=pygame_ess.load_images([page_name, cipher_type]),
                                             frame=coord(47, cipher_type_y_coord, 929, 86, 0, cipher_type_y_coord),
                                             runclass=cipher_types[cipher_type])


#############
# Home Page #
#############
class cryptography:
    '''cryptography home page'''

    def run():
        '''Display cryptography home page'''

        # Load the screen
        pygame_ess.load_screen(screen, cryptography_objects)

        while True:
            # Check for selection
            selection_result = pygame_ess.selection(screen, cryptography_objects)
            selection_result_key, selection_result_value = list(selection_result.keys())[0], list(selection_result.values())[0]
            
            if selection_result_key == 'button':
                if selection_result_value == True: pygame_ess.load_screen(screen, cryptography_objects)
            
            # Kill page
            if pygame_ess.buffer(): return True


#############
# Main loop #
#############
if __name__ == "__main__":
    # Run home screen
    cryptography.run()

    # Done! Time to quit.
    pygame_ess.quit()

