######################################
# Import and initialize the librarys #
######################################
import pygame
import logging
from item_storage import *
from pygame_ess import pygame_ess
from textfield_event import textfield_event


##################
# Initialization #
##################
logging.info('Loading switch mode button...')
screen = pygame.display.set_mode((1024, 768))


#########################
# Variables declaration #
#########################
logging.debug('Initialising monoalphabetic subsitution cipher variables...')
page_name:str = 'mode'
mode_objects:dict = dict()


################################
# Load set mode button objects #
################################
logging.debug('Initialising set mode button objects...')

# Load decrypt mode
mode_objects['decrypt'] = item(name='decrypt',
                               type='button',
                               images=pygame_ess.load_images([page_name, 'decrypt']),
                               frame=coord(
                                        738, 459, 
                                        199, 56, 
                                        738, 459
                                        ),
                               runclass='decrypt')

# Load encrypt mode
mode_objects['encrypt'] = item(name='encrypt',
                               type='button',
                               images=pygame_ess.load_images([page_name, 'encrypt']),
                               frame=coord(
                                        738, 459, 
                                        199, 56, 
                                        738, 459
                                        ),
                               runclass='encrypt')


###################
# Generate surface #
###################
logging.debug('Initialising monoalphabetic subsitution cipher window...')
mode_window:surface = surface(mode_objects, name=page_name)


###########################
# Set mode button Surface #
###########################
class mode:

    mode = 'encrypt'

    def run(window):
        selection_result = pygame_ess.selection_event(mode_window)

        if selection_result['action_result'] == 'decrypt':
            mode = 'encrypt'
        
        elif selection_result['action_result'] == 'encrypt':
            mode = 'decrypt'