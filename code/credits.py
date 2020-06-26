# This file is part of Cryptography GUI, licensed under the MIT License.
# Copyright (c) 2020 Benedict Woo Jun Kai
# See LICENSE.md for more details.


######################################
# Import and initialize the librarys #
######################################
import logging
import webbrowser
from item_storage import *
from pygame_ess import pygame_ess
from common_objects import common_objects

logging.info('Loading credits...')


#########################
# Variables declaration #
#########################
logging.debug('Initialising credits variables...')
page_name:str = 'credits'
credits_objects:dict = dict()


##############################
# Load credits objects #
##############################
logging.debug('Initialising credits objects...')

common_objects.load(credits_objects, page_name, ['back'])

# Button
credits_objects['check_it_out'] = item(name='check_it_out',
                                        type='button',
                                        images=pygame_ess.load.images([page_name, 'check_it_out']),
                                        frame=coord(
                                            266, 906, 
                                            492, 67, 
                                            266, 906),
                                        runclass=webbrowser.open,
                                        runclass_parameter='https://github.com/benwoo1110')


###################
# Generate window #
###################
logging.debug('Initialising caesar cipher window...')
# Load background and back button
credits_window:surface = surface(credits_objects, name=page_name,
                                 frame=coord(bx=0, by=0, w=1024, h=1102, scale=False))


################
# Credits Page #
################
class credits:
    '''Credits page'''

    def run():
        '''Display Credits page'''

        # Load the screen
        pygame_ess.display.screen(credits_window)
        logging.info('Loaded credits window.')

        while True:
            # Check for selection
            selection_result:dict = pygame_ess.event.selection(credits_window, credits_objects)

            # Quit program
            if selection_result['action_result'] == 'quit' or pygame_ess.buffer(credits_window): 
                return 'quit'

            # Button press
            elif selection_result['object_type'] == 'button':
                # Go back to previous page
                if selection_result['action_result'] == 'back': return True

