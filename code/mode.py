######################################
# Import and initialize the librarys #
######################################
import logging
from item_storage import *
from pygame_ess import pygame_ess
from textfield_event import textfield_event
from config import config

logging.info('Loading switch mode button...')


#########################
# Variables declaration #
#########################
logging.debug('Initialising mode switch variables...')
page_name:str = 'mode'
mode_objects:dict = dict()


################################
# Load set mode button objects #
################################
logging.debug('Initialising mode switch objects...')

# Load decrypt mode
mode_objects['decrypt'] = item(name='decrypt',
                               type='button',
                               images=pygame_ess.load.images([page_name, 'decrypt']),
                               frame=coord(
                                        127, 6, 
                                        153, 62, 
                                        0, 0
                                        ),)

# Load encrypt mode
mode_objects['encrypt'] = item(name='encrypt',
                               type='button',
                               images=pygame_ess.load.images([page_name, 'encrypt']),
                               frame=coord(
                                        127, 6, 
                                        153, 62, 
                                        0, 0),
                               runclass='encrypt')


###################
# Generate surface #
###################
logging.debug('Initialising mode button surface...')
mode_window:surface = surface(mode_objects, name=page_name, 
                              frame=coord(bx=694, by=0, w=330, h=100, scale=False))


###########################
# Set mode button Surface #
###########################
class Mode:

    def __init__(self, current_mode:str = 'encrypt'):
        # Variable for mode object
        self.current_mode = current_mode

    # Load the mode button below ciphertext
    def load_button(self, window:surface, objects:dict):
        # Set mode_window position
        mode_window.frame.by = objects['ciphertext'].frame.iy + 112 * config.scale_w()

        # Add mode button to main window
        pygame_ess.load.surface(window.surface, mode_window)

    def set_mode(self, window:surface, objects:dict) -> str:
        # Set to encrypt
        if self.current_mode == 'encrypt':
            # Enable encrypt button
            mode_objects['decrypt'].runclass = None
            mode_objects['encrypt'].runclass = 'encrypt'

            # Change button
            pygame_ess.load.object(mode_window.surface, mode_objects['encrypt'])
            self.load_button(window, objects)

            # Change object runclass of plaintext and ciphertext
            objects['plaintext'].runclass = textfield_event.run
            objects['ciphertext'].runclass = None

            # Log change
            logging.info('Set mode to encrypt.')

        # Set to decrypt
        if self.current_mode == 'decrypt':
            # Enable decrypt button
            mode_objects['encrypt'].runclass = None
            mode_objects['decrypt'].runclass = 'decrypt'

            # Change button
            pygame_ess.load.object(mode_window.surface, mode_objects['decrypt'])
            self.load_button(window, objects)

            # Change object runclass of plaintext and ciphertext
            objects['ciphertext'].runclass = textfield_event.run
            objects['plaintext'].runclass = None

            # Log change
            logging.info('Changed mode to decrypt.')

    # Check of mode button click
    def run(self, window:surface, objects:dict):
        # Grap y-axis location of mode button (due to scrolling)
        mode_window.frame.by = objects['ciphertext'].frame.iy + window.frame.by + 112 * config.scale_w()

        # Check for mode selection
        selection_result = pygame_ess.event.selection(mode_window, mode_objects)

        if selection_result['object_name'] == 'decrypt':
            # Set mode to encrypt
            self.current_mode = 'encrypt'
            # Set to mode
            self.set_mode(window, objects)
        
        elif selection_result['object_name'] == 'encrypt':
            # Set mode decrypt
            self.current_mode = 'decrypt'
            # Set to mode
            self.set_mode(window, objects)
