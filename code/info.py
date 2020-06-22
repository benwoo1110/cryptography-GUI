######################################
# Import and initialize the librarys #
######################################
import logging
import pygame
from pygame_ess import pygame_ess
from item_storage import *
import webbrowser 


##################
# Initialization #
##################
logging.info('Loading info screen...')
screen = pygame.display.set_mode((1024, 768))


########################
# Variables declaration #
########################
logging.debug('Initialising info variables...')
page_name:str = 'info'
info_objects:dict = dict()
info_screen_data:dict = {'atbash_cipher':{'height':1901, 'link':'http://practicalcryptography.com/ciphers/classical-era/atbash-cipher/'},
                     'affine_cipher':{'height':1828, 'link':'http://practicalcryptography.com/ciphers/classical-era/affine/'},
                     'caesar_cipher':{'height':1886, 'link':'http://practicalcryptography.com/ciphers/classical-era/caesar/'},
                     'monoalphabetic_subsitution_cipher':{'height':1819, 'link':'http://practicalcryptography.com/ciphers/classical-era/simple-substitution/'},
                     'polyalphabetic_substitution_cipher':{'height':2010, 'link':'http://practicalcryptography.com/ciphers/classical-era/vigenere-gronsfeld-and-autokey/'}
                    }


##############################
# Load invalid input objects #
##############################
logging.debug('Initialising info input objects...')

# Load all info objects
for cipher_type in info_screen_data.keys():
    info_objects[cipher_type] = item(name=cipher_type, 
                                type='info', 
                                images=pygame_ess.load.images([page_name, cipher_type]),
                                frame=coord(
                                        0, 0,
                                        1024, 2010,
                                        0, 0),)

# Learn more! button
info_objects['learn_more'] = item(name='learn_more', 
                                type='button', 
                                images=pygame_ess.load.images([page_name, 'learn_more']),
                                frame=coord(
                                        451, 2010,
                                        263, 74,
                                        451, 2010
                                        ),
                                runclass='learn_more')

# Try now! button
info_objects['try_now'] = item(name='try_now', 
                                type='button', 
                                images=pygame_ess.load.images([page_name, 'try_now']),
                                frame=coord(
                                        741, 2010,
                                        263, 74,
                                        741, 2010
                                        ),
                                runclass='back')

# Load back button
pygame_ess.load.essential_objects(info_objects, page_name, shares=['back'], background=False)


###################
# Generate window #
###################
logging.debug('Initialising info screen window...')
info_window:surface = surface(info_objects, name=page_name, frame=coord(0, 0, 1024, 2010))


###############
# Info screen #
###############
class info:
    '''cryptography home page'''

    def run(cipher_type:str = 'affine_cipher'):
        '''Display cryptography home page'''

        # Set correct info screen
        # Set height
        info_window.frame.by = 0
        info_window.frame.h = info_screen_data[cipher_type]['height']
        # Set button position
        info_objects['learn_more'].frame.by = info_screen_data[cipher_type]['height'] - 123
        info_objects['learn_more'].frame.iy = info_screen_data[cipher_type]['height'] - 123
        info_objects['try_now'].frame.by = info_screen_data[cipher_type]['height'] - 123
        info_objects['try_now'].frame.iy = info_screen_data[cipher_type]['height'] - 123

        # Load screen
        pygame_ess.display.objects(info_window, info_objects, [cipher_type])

        while True:
            # Check for selection
            selection_result:dict = pygame_ess.event.selection(info_window, info_objects)

            # Quit program
            if selection_result['action_result'] == 'quit' or pygame_ess.buffer(info_window): 
                return 'quit'

            # Close info window
            elif selection_result['action_result'] == 'back': 
                return True

            # Open learn more URL
            elif selection_result['action_result'] == 'learn_more': 
                webbrowser.open(info_screen_data[cipher_type]['link'])


#############
# Main loop #
#############
if __name__ == "__main__":
    pygame.init()
    # Run home screen
    info.run()

    # Done! Time to quit.
    pygame_ess.quit()