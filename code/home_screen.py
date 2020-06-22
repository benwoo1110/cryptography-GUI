######################################
# Import and initialize the librarys #
######################################
import logging
import pygame
from pygame_ess import pygame_ess
from item_storage import *
from atbash_cipher import atbash_cipher
from affine_cipher import affine_cipher
from caesar_cipher import caesar_cipher
from monoalphabetic_subsitution_cipher import monoalphabetic_subsitution_cipher
from polyalphabetic_substitution_cipher import polyalphabetic_substitution_cipher
from common_objects import common_objects


##################
# Initialization #
##################
logging.info('Loading home screen...')
screen = pygame.display.set_mode((1024, 768))


########################
# Variables declaration #
########################
logging.debug('Initialising home screen variables...')
page_name:str = 'cryptography'
cipher_types:dict = {'atbash_cipher':atbash_cipher.run,
                     'affine_cipher':affine_cipher.run,
                     'caesar_cipher':caesar_cipher.run, 
                     'monoalphabetic_subsitution_cipher':monoalphabetic_subsitution_cipher.run, 
                     'polyalphabetic_substitution_cipher':polyalphabetic_substitution_cipher.run
                    }

cryptography_objects:dict = dict()


############################
# Load home screen objects #
############################
logging.debug('Initialising home screen objects...')

# Load essentials images
common_objects.load(cryptography_objects, page_name)

# cipher types view list
for cipher_type in cipher_types:
    cipher_type_y_coord = 112 + list(cipher_types.keys()).index(cipher_type) * 106
    cryptography_objects[cipher_type] = item(name=cipher_type,
                                             type='button',
                                             images=pygame_ess.load.images([page_name, cipher_type]),
                                             frame=coord(
                                                        47, cipher_type_y_coord, 
                                                        929, 86, 
                                                         0, cipher_type_y_coord),
                                             runclass=cipher_types[cipher_type])


###################
# Generate window #
###################
logging.debug('Initialising home screen window...')
cryptography_window:surface = surface(cryptography_objects, name=page_name, frame=coord(0, 0, 1024, 1000))


#############
# Home Page #
#############
class cryptography:
    '''cryptography home page'''

    def run():
        '''Display cryptography home page'''

        # Load the screen
        pygame_ess.display.screen(cryptography_window)
        logging.info('Loaded home screen window.')

        while True:
            # Check for selection
            selection_result:dict = pygame_ess.event.selection(cryptography_window, cryptography_objects)

            # Quit program
            if selection_result['action_result'] == 'quit' or pygame_ess.buffer(cryptography_window): 
                return 'quit'


#############
# Main loop #
#############
if __name__ == "__main__":
    # Run home screen
    pygame.init()
    cryptography.run()

    # Done! Time to quit.
    pygame_ess.quit()

