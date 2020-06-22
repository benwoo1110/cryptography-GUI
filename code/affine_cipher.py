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

logging.info('Loading affine cipher...')

#########################
# Variables declaration #
#########################
logging.debug('Initialising affine cipher variables...')
page_name:str = 'affine_cipher'
affine_cipher_objects: dict = dict()
mode = Mode()


##############################
# Load Affine Cipher objects #
##############################
logging.debug('Initialising affine cipher objects...')

# Load essentials images
common_objects.load(affine_cipher_objects, page_name, ['back', 'info'])

# Textfields
affine_cipher_objects['plaintext'] = item(name='plaintext',
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
                                              325, 158, 
                                              632, 62, 
                                              307, 150
                                              ),
                                          runclass=textfield_event.run)

affine_cipher_objects['a'] = item(name='a',
                                type='textfield',
                                meta=text_data(
                                    text='1',
                                    font_type='Monaco.dfont',
                                    font_size=34,
                                    colour=pygame_ess.colour.black,
                                    validation=validate.digits(min_num=1, max_num=26)
                                    ),
                                images=pygame_ess.load.images([page_name, 'a']),
                                frame=coord(
                                    325, 248, 
                                    160, 62, 
                                    307, 238
                                    ),
                                runclass=textfield_event.run)     

affine_cipher_objects['b'] = item(name='b',
                                type='textfield',
                                meta=text_data(
                                    text='2',
                                    font_type='Monaco.dfont',
                                    font_size=34,
                                    colour=pygame_ess.colour.black,
                                    validation=validate.digits(min_num=1, max_num=26)
                                    ),
                                images=pygame_ess.load.images([page_name, 'b']),
                                frame=coord(
                                    569, 247, 
                                    160, 62, 
                                    551, 238
                                    ),
                                runclass=textfield_event.run)   

affine_cipher_objects['ciphertext'] = item(name='ciphertext',
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
                                              325, 535, 
                                              632, 62, 
                                              307, 526),)


###################
# Generate window #
###################
logging.debug('Initialising affine cipher window...')
affine_cipher_window:surface = surface(affine_cipher_objects, name=page_name)


######################
# Affine Cipher Page #
######################
class affine_cipher:
    '''Affine Cipher Page'''

    def encrypt() -> str:
        ''' Encrypt plaintext'''

        # Get plaintext and keys
        plaintext:str = affine_cipher_objects['plaintext'].meta.text
        a:int = int(affine_cipher_objects['a'].meta.text)
        b:int = int(affine_cipher_objects['b'].meta.text)

        # Variables
        alphabet = pygame_ess.alphabet

        # Encode from A-Z
        replaced = ''
        for char_index in range(26):
            replaced += alphabet[ (a * char_index + b) % 26 ]

        # Calculate ciphertext
        ciphertext:str = ''
        for char in plaintext:
            if char.isalpha():
                cipherchar:str = replaced[alphabet.find(char.upper())]
                if char.islower(): cipherchar = cipherchar.lower()
                ciphertext += cipherchar

            else: ciphertext += char

        # Save back to ciphertext object
        affine_cipher_objects['ciphertext'].meta.text = ciphertext
        # Update screen
        pygame_ess.display.object(affine_cipher_window, affine_cipher_objects['ciphertext'])        

        return ciphertext

    def decrypt() -> str:
        ''' Decrypt ciphertext'''

        # Get ciphertext and keys
        ciphertext:str = str(affine_cipher_objects['ciphertext'].meta.text)
        a:int = int(affine_cipher_objects['a'].meta.text)
        b:int = int(affine_cipher_objects['b'].meta.text)

        # Variables
        alphabet = pygame_ess.alphabet

        # Decode from A-Z
        replaced = ''
        for char_index in range(26):
            replaced += alphabet[ (a * char_index + b) % 26 ]

        # Calculate plaintext
        plaintext:str = ''
        for char in ciphertext:
            if char.isalpha():
                plainchar:str = alphabet[replaced.find(char.upper())]
                if char.islower(): plainchar = plainchar.lower()
                plaintext += plainchar

            else: plaintext += char
            

        # Save back to plaintext object
        affine_cipher_objects['plaintext'].meta.text = plaintext
        # Update screen
        pygame_ess.display.object(affine_cipher_window, affine_cipher_objects['plaintext'])        

        return plaintext


    def run():
        '''Display Affine Cipher Page'''

        # Load mode button
        mode.set_mode(affine_cipher_window, affine_cipher_objects)

        # Set info button runclass
        affine_cipher_objects['info'].runclass = info.run
        affine_cipher_objects['info'].runclass_parameter = page_name

        # Load screen
        affine_cipher.encrypt()
        logging.info('Loaded affine cipher window.')

        while True:
            # Check for selection
            selection_result:dict = pygame_ess.event.selection(affine_cipher_window, affine_cipher_objects)

            # Check of mode button press
            mode.run(affine_cipher_window, affine_cipher_objects)

            # Quit program
            if selection_result['action_result'] == 'quit' or pygame_ess.buffer(affine_cipher_window): 
                return 'quit'

            # Button press
            elif selection_result['object_type'] == 'button':
                # Go back to previous page
                if selection_result['action_result'] == 'back': return True
            
            # Textfield updated
            elif selection_result['object_type'] == 'textfield':
                # encrypt to ciphertext
                if mode.current_mode == 'encrypt': affine_cipher.encrypt()
                # decrypt to plaintext
                elif mode.current_mode == 'decrypt': affine_cipher.decrypt()


#############
# Main loop #
#############
if __name__ == "__main__":
    # Run home screen
    pygame.init()
    affine_cipher.run()

    # Done! Time to quit.
    pygame_ess.quit()