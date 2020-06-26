# This file is part of Cryptography GUI, licensed under the MIT License.
# Copyright (c) 2020 Benedict Woo Jun Kai
# See LICENSE.md for more details.


######################################
# Import and initialize the librarys #
######################################
import logging
import webbrowser 
from pygame_ess import pygame_ess
from item_storage import *
from common_objects import common_objects
from config import config

logging.info('Loading info screen...')


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

# Load back button
common_objects.load(info_objects, page_name, shares=['back'], background=False)

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


###################
# Generate window #
###################
logging.debug('Initialising info screen window...')
info_window:surface = surface(info_objects, name=page_name, 
                              frame=coord(0, 0, 1024, 2010, scale=False))


###############
# Info screen #
###############
class info:
    '''cryptography home page'''

    def run(cipher_type:str = 'affine_cipher'):
        '''Display cryptography home page'''

        # Ensure cipher_type exist
        if cipher_type not in info_screen_data.keys(): 
            logging.error('[{}] No such cipher type for the info screen.'.format(info_window.name))
            return True

        # Set correct info screen
        # Set height
        info_window.frame.by = 0
        info_window.frame.h = int(info_screen_data[cipher_type]['height'] * config.scale_w())
        # Set button position
        info_objects['learn_more'].frame.by = int( (info_screen_data[cipher_type]['height'] - 123)  * config.scale_w())
        info_objects['learn_more'].frame.iy = int( (info_screen_data[cipher_type]['height'] - 123)  * config.scale_w())
        info_objects['try_now'].frame.by = int( (info_screen_data[cipher_type]['height'] - 123)  * config.scale_w())
        info_objects['try_now'].frame.iy = int( (info_screen_data[cipher_type]['height'] - 123)  * config.scale_w())

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