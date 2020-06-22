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

logging.info('Loading caesar cipher...')


#########################
# Variables declaration #
#########################
logging.debug('Initialising caesar cipher variables...')
page_name:str = 'caesar_cipher'
caesar_cipher_objects:dict = dict()
mode = Mode()


##############################
# Load affine cipher objects #
##############################
logging.debug('Initialising caesar cipher objects...')

# Load essentials images
common_objects.load(caesar_cipher_objects, page_name, ['back', 'info'])

# Textfield
caesar_cipher_objects['plaintext'] = item(name='plaintext',
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
                                              307, 146),
                                          runclass=textfield_event.run)

caesar_cipher_objects['key'] = item(name='key',
                                          type='textfield',
                                          meta=text_data(
                                              text='1',
                                              font_type='Monaco.dfont',
                                              font_size=34,
                                              colour=pygame_ess.colour.black,
                                              validation=validate.digits()
                                              ),
                                          images=pygame_ess.load.images([page_name, 'key']),
                                          frame=coord(
                                              325, 238, 
                                              160, 62, 
                                              307, 229),
                                          runclass=textfield_event.run)

caesar_cipher_objects['alphabet'] = item(name='alphabet',
                                          type='textfield',
                                          meta=text_data(
                                              text='"ABCDEFGHIJKLMNOPQRSTUVWXYZ"',
                                              font_type='Monaco.dfont',
                                              font_size=34,
                                              colour=pygame_ess.colour.white
                                              ),
                                          images=pygame_ess.load.images([page_name, 'alphabet']),
                                          frame=coord(
                                              311, 403, 
                                              649, 47, 
                                              311, 403),)

caesar_cipher_objects['replaced'] = item(name='replaced',
                                         type='textfield',
                                         meta=text_data(
                                                text='"ABCDEFGHIJKLMNOPQRSTUVWXYZ"',
                                                font_type='Monaco.dfont',
                                                font_size=34,
                                                colour=pygame_ess.colour.white
                                                ),
                                         images=pygame_ess.load.images([page_name, 'replaced']),
                                         frame=coord(
                                                311, 464, 
                                                649, 47, 
                                                311, 464),)

caesar_cipher_objects['ciphertext'] = item(name='ciphertext',
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
logging.debug('Initialising caesar cipher window...')
caesar_cipher_window:surface = surface(caesar_cipher_objects, name=page_name)


######################
# Caesar Cipher Page #
######################
class caesar_cipher:
    '''Caesar Cipher Page'''

    def encrypt() -> str:
        ''' Encrypt plaintext'''

        # Get plaintext and keys
        plaintext:str = str(caesar_cipher_objects['plaintext'].meta.text)
        key:int = int(caesar_cipher_objects['key'].meta.text)

        alphablet = pygame_ess.alphabet
        replaced = alphablet[key%26:] + alphablet[:key%26]
        
        caesar_cipher_objects['replaced'].meta.text = '"'+replaced+'"'
       
        ciphertext:str = ''

        # Convert to ciphertext
        for char in plaintext:
            if char.isalpha():
                cipherchar:str = replaced[alphablet.index(char.upper())]
                if not char.isupper(): cipherchar = cipherchar.lower()
                ciphertext += cipherchar

            else: ciphertext += char

        # Save it to data
        caesar_cipher_objects['ciphertext'].meta.text = ciphertext
        # Print data to screen
        pygame_ess.display.objects(caesar_cipher_window, caesar_cipher_objects, ['replaced', 'ciphertext'])

        return ciphertext

    def decrypt() -> str:
        ''' Decrypt ciphertext'''

        # Get ciphertext and keys
        try: 
            ciphertext:str = str(caesar_cipher_objects['ciphertext'].meta.text)
            key:int = int(caesar_cipher_objects['key'].meta.text)
        except:
            print('type error')
            return

        alphablet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        replaced = alphablet[key%26:] + alphablet[:key%26]
        
        caesar_cipher_objects['replaced'].meta.text = '"'+replaced+'"'
       
        plaintext:str = ''

        # Convert to ciphertext
        for char in ciphertext:
            if char.isalpha():
                plainchar:str = alphablet[replaced.index(char.upper())]
                if not char.isupper(): plainchar = plainchar.lower()
                plaintext += plainchar

            else: ciphertext += char

        # Save it to data
        caesar_cipher_objects['plaintext'].meta.text = plaintext
        # Print data to screen
        pygame_ess.display.objects(caesar_cipher_window, caesar_cipher_objects, ['replaced', 'plaintext'])


        return plaintext
    
    def run():
        '''Display Caesar Cipher Page'''
        
        # Load mode button
        mode.set_mode(caesar_cipher_window, caesar_cipher_objects)

        # Set info button runclass
        caesar_cipher_objects['info'].runclass = info.run
        caesar_cipher_objects['info'].runclass_parameter = page_name

        # Load the screen
        caesar_cipher.encrypt()
        logging.info('Loaded caesar cipher window.')
         
        while True:
            # Check for selection
            selection_result:dict = pygame_ess.event.selection(caesar_cipher_window, caesar_cipher_objects)

            # Check of mode button press
            mode.run(caesar_cipher_window, caesar_cipher_objects)

            # Quit program
            if selection_result['action_result'] == 'quit' or pygame_ess.buffer(caesar_cipher_window): 
                return 'quit'

            # Button press
            elif selection_result['object_type'] == 'button':
                # Go back to previous page
                if selection_result['action_result'] == 'back': return True
            
            # Textfield updated
            elif selection_result['object_type'] == 'textfield':
                # encrypt to ciphertext
                if mode.current_mode == 'encrypt': caesar_cipher.encrypt()
                # decrypt to plaintext
                elif mode.current_mode == 'decrypt': caesar_cipher.decrypt()


#############
# Main loop #
#############
if __name__ == "__main__":
    pygame.init()
    # Run home screen
    caesar_cipher.run()

    # Done! Time to quit.
    pygame_ess.quit()
