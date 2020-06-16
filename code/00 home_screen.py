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
screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("Cryptography")


########################
# Variables declaration #
########################
page_name = 'cryptography'

cipher_types = {'atbash_cipher':atbash_cipher.run,
                'affine_cipher':affine_cipher.run,
                'caesar_cipher':caesar_cipher.run, 
                'monoalphabetic_subsitution_cipher':monoalphabetic_subsitution_cipher.run, 
                'polyalphabetic_substitution_cipher':polyalphabetic_substitution_cipher.run
                }

cryptography_objects = dict()


############################
# Load home screen objects #
############################

# Load essentials images
pygame_ess.load_essential_objects(cryptography_objects, page_name)

# cipher types view list
for cipher_type in cipher_types.keys():
    cipher_type_y_coord = 112 + list(cipher_types.keys()).index(cipher_type) * 106
    cryptography_objects[cipher_type] = item(name=cipher_type,
                                             type='button',
                                             images=pygame_ess.load_images([page_name, cipher_type]),
                                             frame=coord(47, cipher_type_y_coord, 929, 86, 0, cipher_type_y_coord),
                                             runclass=cipher_types[cipher_type])


###################
# Generate window #
###################
cryptography_window = surface(cryptography_objects, frame=coord(0, 0, 1024, 1000))


#############
# Home Page #
#############
class cryptography:
    '''cryptography home page'''

    def run():
        '''Display cryptography home page'''

        # Load the screen
        pygame_ess.load_screen(cryptography_window)

        while True:
            # Check for selection
            selection_result = pygame_ess.selection_event(cryptography_window, cryptography_objects)

            # Quit program
            if selection_result['action_result'] == 'quit' or pygame_ess.buffer(cryptography_window): 
                return 'quit'


#############
# Main loop #
#############
if __name__ == "__main__":
    # Run home screen
    cryptography.run()

    # Done! Time to quit.
    pygame_ess.quit()

