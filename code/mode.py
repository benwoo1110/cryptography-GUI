######################################
# Import and initialize the librarys #
######################################
import logging
import pygame
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
mode_window:surface = surface(mode_objects, name=page_name, frame=coord(bx=694, by=0, w=330, h=100))


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
        mode_window.frame.by = objects['ciphertext'].frame.iy + 104

        # Add mode button to main window
        Window = window.Window
        Window.blit(mode_window.Window, mode_window.frame.box_coord())

        # Load to screen
        pygame_ess.display.screen(window)

    def set_mode(self, window:surface, objects:dict) -> str:
        # Set to encrypt
        if self.current_mode == 'encrypt':
            # Enable encrypt button
            mode_objects['decrypt'].runclass = None
            mode_objects['encrypt'].runclass = 'encrypt'

            # Change button
            pygame_ess.load.object(mode_window.Window, mode_objects['encrypt'])
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
            pygame_ess.load.object(mode_window.Window, mode_objects['decrypt'])
            self.load_button(window, objects)

            # Change object runclass of plaintext and ciphertext
            objects['ciphertext'].runclass = textfield_event.run
            objects['plaintext'].runclass = None

            # Log change
            logging.info('Changed mode to decrypt.')

    # Check of mode button click
    def run(self, window:surface, objects:dict):
        # Grap y-axis location of mode button (due to scrolling)
        mode_window.frame.by = objects['ciphertext'].frame.iy + window.frame.by + 104

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
