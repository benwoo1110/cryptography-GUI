# This file is part of Cryptography GUI, licensed under the MIT License.
# Copyright (c) 2020 Benedict Woo Jun Kai
# See LICENSE.md for more details.


######################################
# Import and initialize the librarys #
######################################
import logging
from item_storage import *
from pygame_ess import pygame_ess
from mode import Mode
from textfield_event import textfield_event
from input_validation import validate
from info import info
from common_objects import common_objects

logging.info('Loading atbash cipher...')


#########################
# Variables declaration #
#########################
logging.debug('Initialising atbash cipher variables...')
page_name:str = 'atbash_cipher'
atbash_cipher_objects:dict = dict()
mode = Mode()


##############################
# Load affine cipher objects #
##############################
logging.debug('Initialising atbash cipher objects...')

# background image
common_objects.load(atbash_cipher_objects, page_name, ['back', 'info'])

# Textfield
atbash_cipher_objects['plaintext'] = item(name='plaintext',
                                          type='textfield',
                                          meta=text_data(
                                              text='plaintext',
                                              font_type='Monaco.dfont',
                                              font_size=34,
                                              colour=pygame_ess.colour.black,
                                              validation=validate.text()
                                              ),
                                          images=pygame_ess.load.images([page_name, 'plaintext']),
                                          frame=coord(
                                              325, 156, 
                                              632, 62, 
                                              307, 146
                                              ),
                                          runclass=textfield_event.run)

atbash_cipher_objects['ciphertext'] = item(name='ciphertext',
                                          type='textfield',
                                          meta=text_data(
                                              text='ciphertext',
                                              font_type='Monaco.dfont',
                                              font_size=34,
                                              colour=pygame_ess.colour.black,
                                              validation=validate.text()
                                              ),
                                          images=pygame_ess.load.images([page_name, 'ciphertext']),
                                          frame=coord(
                                              325, 542, 
                                              632, 62, 
                                              307, 533),)


###################
# Generate window #
###################
logging.debug('Initialising atbash cipher window...')
atbash_cipher_window:surface = surface(atbash_cipher_objects, name=page_name,
                                       frame=coord(0, 0, 1024, 768, scale=False))


######################
# Atbash Cipher Page #
######################
class atbash_cipher:
    '''Atbash Cipher Page'''

    def encrypt() -> str:
        ''' Encrypt plaintext'''

        # Get plaintext
        plaintext:str = atbash_cipher_objects['plaintext'].meta.text

        # Variables
        alphabet = pygame_ess.alphabet
        replace = alphabet[::-1]

        # Calculate ciphertext
        ciphertext:str = ''
        for char in plaintext:
            if char.isalpha():
                cipherchar:str = replace[alphabet.find(char.upper())]
                if char.islower(): cipherchar = cipherchar.lower()
                ciphertext += cipherchar

            else: ciphertext += char

        # Output to screen
        atbash_cipher_objects['ciphertext'].meta.text = ciphertext
        pygame_ess.display.object(atbash_cipher_window, atbash_cipher_objects['ciphertext'])

        return ciphertext

    def decrypt() -> str:
        ''' Decrypt ciphertext'''

        # Get plaintext
        ciphertext:str = atbash_cipher_objects['ciphertext'].meta.text

        # Variables
        alphabet = pygame_ess.alphabet
        replace = alphabet[::-1]

        # Calculate ciphertext
        plaintext:str = ''
        for char in ciphertext:
            if char.isalpha():
                plainchar:str = alphabet[replace.find(char.upper())]
                if char.islower(): plainchar = plainchar.lower()
                plaintext += plainchar

            else: plaintext += char

        # Output to screen
        atbash_cipher_objects['plaintext'].meta.text = plaintext
        pygame_ess.display.object(atbash_cipher_window, atbash_cipher_objects['plaintext'])

        return plaintext

    def run():
        '''Display Atbash Cipher Page'''

        # Load mode button
        mode.set_mode(atbash_cipher_window, atbash_cipher_objects)

        # Set info button runclass
        atbash_cipher_objects['info'].runclass = info.run
        atbash_cipher_objects['info'].runclass_parameter = page_name

        # Load the screen
        pygame_ess.display.screen(atbash_cipher_window, animate=True)
        atbash_cipher.encrypt()
        logging.info('Loaded atbash cipher window.')
         
        while True:
            # Check for selection
            selection_result:dict = pygame_ess.event.selection(atbash_cipher_window, atbash_cipher_objects)

            # Check of mode button press
            mode.run(atbash_cipher_window, atbash_cipher_objects)

            # Quit program
            if selection_result['action_result'] == 'quit' or pygame_ess.buffer(atbash_cipher_window): 
                return 'quit'

            # Button press
            elif selection_result['object_type'] == 'button':
                # Go back to previous page
                if selection_result['action_result'] == 'back': return True
            
            # Textfield updated
            elif selection_result['object_type'] == 'textfield':
                # encrypt to ciphertext
                if mode.current_mode == 'encrypt': atbash_cipher.encrypt()
                # decrypt to plaintext
                elif mode.current_mode == 'decrypt': atbash_cipher.decrypt()


#############
# Main loop #
#############
if __name__ == "__main__":
    pygame.init()
    # Run home screen
    atbash_cipher.run()

    # Done! Time to quit.
    pygame_ess.quit()