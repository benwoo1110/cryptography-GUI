######################################
# Import and initialize the librarys #
######################################
import logging
import pygame
import random
from item_storage import *
from pygame_ess import pygame_ess
from mode import Mode
from textfield_event import textfield_event
from input_validation import validate
from info import info


##################
# Initialization #
##################
logging.info('Loading monoalphabetic subsitution cipher...')
screen = pygame.display.set_mode((1024, 768))

#########################
# Variables declaration #
#########################
logging.debug('Initialising monoalphabetic subsitution cipher variables...')
page_name:str = 'monoalphabetic_subsitution_cipher'
monoalphabetic_subsitution_cipher_objects:dict = dict()
mode = Mode()


##############################
# Load affine cipher objects #
##############################
logging.debug('Initialising monoalphabetic subsitution cipher objects...')

# Load essentials images
pygame_ess.load_essential_objects(monoalphabetic_subsitution_cipher_objects, page_name, ['back', 'info'])

# Button
monoalphabetic_subsitution_cipher_objects['shuffle'] = item(name='shuffle',
                                              type='button',
                                              images=pygame_ess.load_images([page_name, 'shuffle']),
                                              frame=coord(
                                                  738, 459, 
                                                  199, 56, 
                                                  738, 459),
                                              runclass='shuffle')

# Textfield
monoalphabetic_subsitution_cipher_objects['plaintext'] = item(name='plaintext',
                                          type='textfield',
                                          meta=text_data(
                                              text='plaintext',
                                              font_type='Monaco.dfont',
                                              font_size=34,
                                              colour=pygame_ess.colour.black,
                                              validation=validate.text()
                                              ),
                                          images=pygame_ess.load_images([page_name, 'plaintext']),
                                          frame=coord(
                                              325, 175, 
                                              632, 62, 
                                              307, 165),
                                          runclass=textfield_event.run)

monoalphabetic_subsitution_cipher_objects['alphabet'] = item(name='alphabet',
                                          type='textfield',
                                          meta=text_data(
                                              text='"ABCDEFGHIJKLMNOPQRSTUVWXYZ"',
                                              font_type='Monaco.dfont',
                                              font_size=34,
                                              colour=pygame_ess.colour.white
                                              ),
                                          images=pygame_ess.load_images([page_name, 'alphabet']),
                                          frame=coord(
                                              325, 314, 
                                              632, 62, 
                                              325, 314),)

monoalphabetic_subsitution_cipher_objects['key'] = item(name='key',
                                          type='textfield',
                                          meta=text_data(
                                              text='"ABCDEFGHIJKLMNOPQRSTUVWXYZ"',
                                              font_type='Monaco.dfont',
                                              font_size=34,
                                              colour=pygame_ess.colour.black,
                                              validation=validate.text()
                                              ),
                                          images=pygame_ess.load_images([page_name, 'key']),
                                          frame=coord(
                                              325, 385, 
                                              632, 62, 
                                              307, 375),)

monoalphabetic_subsitution_cipher_objects['ciphertext'] = item(name='ciphertext',
                                          type='textfield',
                                          meta=text_data(
                                              text='ciphertext',
                                              font_type='Monaco.dfont',
                                              font_size=34,
                                              colour=pygame_ess.colour.black,
                                              validation=validate.text()
                                              ),
                                          images=pygame_ess.load_images([page_name, 'ciphertext']),
                                          frame=coord(
                                              325, 611, 
                                              632, 62, 
                                              307, 601),)


###################
# Generate window #
###################
logging.debug('Initialising monoalphabetic subsitution cipher window...')
monoalphabetic_subsitution_cipher_window:surface = surface(monoalphabetic_subsitution_cipher_objects, 
                                                           name=page_name, 
                                                           frame=coord(bx=0,by=0,w=1024,h=810))


##########################################
# Monoalphabetic Subsitution Cipher Page #
##########################################
class monoalphabetic_subsitution_cipher:
    '''Monoalphabetic Subsitution Cipher Page'''

    def shuffle() -> str:
        ''' Shuffle key'''

        # Shuffle the key
        shuffled_alphabet:list = list(pygame_ess.alphabet)
        random.shuffle(shuffled_alphabet)
        monoalphabetic_subsitution_cipher_objects['key'].meta.text = '"' +  ''.join(shuffled_alphabet) + '"'

        # Update key text        
        textfield_event.update_textfield(monoalphabetic_subsitution_cipher_window, monoalphabetic_subsitution_cipher_objects['key'], selected=False)
        
        # encrypt to ciphertext
        if mode.current_mode == 'encrypt': monoalphabetic_subsitution_cipher.encrypt()
        # decrypt to plaintext
        elif mode.current_mode == 'decrypt': monoalphabetic_subsitution_cipher.decrypt()

        return shuffled_alphabet

    def encrypt() -> str:
        ''' Encrypt plaintext'''

        # Get plaintext and key
        plaintext = monoalphabetic_subsitution_cipher_objects['plaintext'].meta.text
        alphabet = pygame_ess.alphabet
        key = monoalphabetic_subsitution_cipher_objects['key'].meta.text[1:-1]

        # Calculate ciphertext
        ciphertext:str = ''
        for char in plaintext:
            if char.isalpha():
                cipherchar:str = key[alphabet.index(char.upper())]
                if char.islower(): cipherchar = cipherchar.lower()

                ciphertext += cipherchar
                
            else: ciphertext += char

        # Stores ciphertext
        monoalphabetic_subsitution_cipher_objects['ciphertext'].meta.text = ciphertext

        # Update screen
        textfield_event.update_textfield(monoalphabetic_subsitution_cipher_window, monoalphabetic_subsitution_cipher_objects['ciphertext'], False)

        return ciphertext

    def decrypt() -> str:
        ''' Decrypt ciphertext'''
        # Get ciphertext and key
        ciphertext = monoalphabetic_subsitution_cipher_objects['ciphertext'].meta.text
        alphabet = pygame_ess.alphabet
        key = monoalphabetic_subsitution_cipher_objects['key'].meta.text[1:-1]

        # Calculate plaintext
        plaintext:str = ''
        for char in ciphertext:
            if char.isalpha():
                plainchar:str = alphabet[key.index(char.upper())]
                if char.islower(): plainchar = plainchar.lower()

                plaintext += plainchar
                
            else: plaintext += char

        # Stores ciphertext
        monoalphabetic_subsitution_cipher_objects['plaintext'].meta.text = plaintext

        # Update screen
        textfield_event.update_textfield(monoalphabetic_subsitution_cipher_window, monoalphabetic_subsitution_cipher_objects['plaintext'], False)
    
        return plaintext

    def run():
        '''Display Monoalphabetic Subsitution Cipher Page'''

        # Load mode button
        mode.set_mode(monoalphabetic_subsitution_cipher_window, monoalphabetic_subsitution_cipher_objects)
        
        # Set info button runclass
        monoalphabetic_subsitution_cipher_objects['info'].runclass = info.run
        monoalphabetic_subsitution_cipher_objects['info'].runclass_parameter = page_name
        
        # Load screen
        monoalphabetic_subsitution_cipher.shuffle()
        logging.info('Loaded monoalphabetic subsitution cipher window.')

        while True:
            # Check for selection
            selection_result:dict = pygame_ess.selection_event(monoalphabetic_subsitution_cipher_window, monoalphabetic_subsitution_cipher_objects)

            # Check of mode button press
            mode.run(monoalphabetic_subsitution_cipher_window, monoalphabetic_subsitution_cipher_objects)

            # Quit program
            if selection_result['action_result'] == 'quit' or pygame_ess.buffer(monoalphabetic_subsitution_cipher_window): 
                return 'quit'
            
            # Button press
            elif selection_result['object_type'] == 'button':
                # Go back to previous page
                if selection_result['action_result'] == 'back': return True
                # Shuffle the key
                elif selection_result['action_result'] == 'shuffle': monoalphabetic_subsitution_cipher.shuffle()
            
            # Textfield updated
            elif selection_result['object_type'] == 'textfield':
                # encrypt to ciphertext
                if mode.current_mode == 'encrypt': monoalphabetic_subsitution_cipher.encrypt()
                # decrypt to plaintext
                elif mode.current_mode == 'decrypt': monoalphabetic_subsitution_cipher.decrypt()


#############
# Main loop #
#############
if __name__ == "__main__":
    pygame.init()
    # Run home screen
    monoalphabetic_subsitution_cipher.run()

    # Done! Time to quit.
    pygame_ess.quit()