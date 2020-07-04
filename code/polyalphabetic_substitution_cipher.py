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

logging.info('Loading polyalphabetic subsitution cipher...')


#########################
# Variables declaration #
#########################
logging.debug('Initialising polyalphabetic subsitution variables...')
page_name:str = 'polyalphabetic_substitution_cipher'
polyalphabetic_substitution_cipher_objects:dict = dict()
mode = Mode()


##############################
# Load affine cipher objects #
##############################
logging.debug('Initialising polyalphabetic subsitution objects...')

# Load essentials images
common_objects.load(polyalphabetic_substitution_cipher_objects, page_name, ['back', 'info'])

# Textfield
polyalphabetic_substitution_cipher_objects['keyword'] = item(name='keyword',
                                          type='textfield',
                                          meta=text_data(
                                              text='KEYWORD',
                                              font_type='Monaco.dfont',
                                              font_size=34,
                                              colour=pygame_ess.colour.black,
                                              validation=validate.text()
                                              ),
                                          images=pygame_ess.load.images([page_name, 'keyword']),
                                          frame=coord(
                                              325, 176, 
                                              632, 62, 
                                              307, 165),
                                          runclass=textfield_event.run)

polyalphabetic_substitution_cipher_objects['plaintext'] = item(name='plaintext',
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
                                              325, 257, 
                                              632, 62, 
                                              307, 248),
                                          runclass=textfield_event.run)

polyalphabetic_substitution_cipher_objects['text'] = item(name='text',
                                          type='textfield',
                                          meta=text_data(
                                              text='text',
                                              font_type='Monaco.dfont',
                                              font_size=34,
                                              colour=pygame_ess.colour.white
                                              ),
                                          images=pygame_ess.load.images([page_name, 'text']),
                                          frame=coord(
                                              325, 382, 
                                              632, 62, 
                                              325, 381),)

polyalphabetic_substitution_cipher_objects['key'] = item(name='key',
                                          type='textfield',
                                          meta=text_data(
                                              text='key',
                                              font_type='Monaco.dfont',
                                              font_size=34,
                                              colour=pygame_ess.colour.white
                                              ),
                                          images=pygame_ess.load.images([page_name, 'key']),
                                          frame=coord(
                                              325, 439, 
                                              632, 62, 
                                              307, 437),)

polyalphabetic_substitution_cipher_objects['ciphertext'] = item(name='ciphertext',
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
                                              325, 574, 
                                              632, 62, 
                                              307, 564),)


###################
# Generate window #
###################
logging.debug('Initialising polyalphabetic subsitution window...')
polyalphabetic_substitution_cipher_window:surface = surface(polyalphabetic_substitution_cipher_objects, name=page_name,
                                                            frame=coord(bx=0, by=0, w=1024, h=768, scale=False))


###########################################
# Polyalphabetic Substitution Cipher Page #
###########################################
class polyalphabetic_substitution_cipher:
    '''Polyalphabetic Substitution Cipher Page'''

    def encrypt() -> str:
        ''' Encrypt plaintext'''

        # Get keyword and plaintext
        keyword:str = polyalphabetic_substitution_cipher_objects['keyword'].meta.text
        plaintext:str = polyalphabetic_substitution_cipher_objects['plaintext'].meta.text

        # Variables
        alphabet:str = pygame_ess.alphabet
        
        # Update text
        polyalphabetic_substitution_cipher_objects['text'].meta.text = plaintext

        # Generate key
        plaintext_length:int = len(plaintext)
        keyword_length:int = len(keyword)
        key:str = keyword.upper() * (plaintext_length//keyword_length) + keyword.upper()[:plaintext_length%keyword_length]

        # Stores key
        polyalphabetic_substitution_cipher_objects['key'].meta.text = key

        # Calculate ciphertext
        ciphertext:str = ''
        for char in range(plaintext_length):
            if plaintext[char].isalpha():
                cipherchar:str = alphabet[ ( alphabet.find(plaintext[char].upper()) + alphabet.find(key[char].upper()) ) % 26 ]
                if plaintext[char].islower(): cipherchar = cipherchar.lower()
                ciphertext += cipherchar

            else: ciphertext += plaintext[char]

        # Stores ciphertext
        polyalphabetic_substitution_cipher_objects['ciphertext'].meta.text = ciphertext
        # Output to screen
        pygame_ess.display.objects(polyalphabetic_substitution_cipher_window, polyalphabetic_substitution_cipher_objects, ['text', 'key', 'ciphertext'])

        return ciphertext

    def decrypt() -> str:
        ''' Decrypt ciphertext'''

        # Get keyword and plaintext
        keyword:str = polyalphabetic_substitution_cipher_objects['keyword'].meta.text
        ciphertext:str = polyalphabetic_substitution_cipher_objects['ciphertext'].meta.text

        # Variables
        alphabet:str = pygame_ess.alphabet

        # Generate key
        ciphertext_length:int = len(ciphertext)
        keyword_length:int = len(keyword)
        key:str = keyword.upper() * (ciphertext_length//keyword_length) + keyword.upper()[:ciphertext_length%keyword_length]
        print(key)
        # Stores key
        polyalphabetic_substitution_cipher_objects['key'].meta.text = key

        # Calculate ciphertext
        plaintext:str = ''
        for char in range(ciphertext_length):
            if ciphertext[char].isalpha():
                if alphabet.find(ciphertext[char].upper()) >= alphabet.find(key[char]): plainchar:str = alphabet[alphabet.find(ciphertext[char].upper()) - alphabet.find(key[char])]
                else: 
                    print(ciphertext[char].upper(), key[char], char)
                    plainchar:str = alphabet[alphabet.find(ciphertext[char].upper()) + 26 - alphabet.find(key[char])]

                if ciphertext[char].islower(): plainchar = plainchar.lower()
                plaintext += plainchar
            
            else: plaintext += ciphertext[char]

        # Stores ciphertext
        polyalphabetic_substitution_cipher_objects['plaintext'].meta.text = plaintext

        # Update text
        polyalphabetic_substitution_cipher_objects['text'].meta.text = plaintext
        # Output to screen
        pygame_ess.display.objects(polyalphabetic_substitution_cipher_window, polyalphabetic_substitution_cipher_objects, ['text', 'key', 'plaintext'])

        return plaintext

    def run():
        '''Polyalphabetic Substitution Cipher Page'''

        # Load mode button
        mode.set_mode(polyalphabetic_substitution_cipher_window, polyalphabetic_substitution_cipher_objects)     
        
        # Set info button runclass
        polyalphabetic_substitution_cipher_objects['info'].runclass = info.run
        polyalphabetic_substitution_cipher_objects['info'].runclass_parameter = page_name
        
        # Load screen
        pygame_ess.display.screen(polyalphabetic_substitution_cipher_window, animate=True)
        polyalphabetic_substitution_cipher.encrypt()
        logging.info('Loaded polyalphabetic subsitution window.')

        while True:
            # Check for selection
            selection_result:dict = pygame_ess.event.selection(polyalphabetic_substitution_cipher_window, polyalphabetic_substitution_cipher_objects)

            # Check of mode button press
            mode.run(polyalphabetic_substitution_cipher_window, polyalphabetic_substitution_cipher_objects)

            # Quit program
            if selection_result['action_result'] == 'quit' or pygame_ess.buffer(polyalphabetic_substitution_cipher_window): 
                return 'quit'
            
            # Button press
            elif selection_result['object_type'] == 'button':
                # Go back to previous page
                if selection_result['action_result'] == 'back': return True
            
            # Textfield updated
            elif selection_result['object_type'] == 'textfield':
                # encrypt to ciphertext
                if mode.current_mode == 'encrypt': polyalphabetic_substitution_cipher.encrypt()
                # decrypt to plaintext
                elif mode.current_mode == 'decrypt': polyalphabetic_substitution_cipher.decrypt()



#############
# Main loop #
#############
if __name__ == "__main__":
    # Run home screen
    polyalphabetic_substitution_cipher.run()

    # Done! Time to quit.
    pygame_ess.quit()