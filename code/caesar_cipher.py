######################################
# Import and initialize the librarys #
######################################
import pygame
import logging
from item_storage import *
from pygame_ess import pygame_ess
from textfield_event import textfield_event
from input_validation import validate


##################
# Initialization #
##################
logging.info('Loading caesar cipher...')
screen = pygame.display.set_mode((1024, 768))


#########################
# Variables declaration #
#########################
logging.debug('Initialising caesar cipher variables...')

page_name:str = 'caesar_cipher'
caesar_cipher_objects:dict = dict()


##############################
# Load affine cipher objects #
##############################
logging.debug('Initialising caesar cipher objects...')

# Load essentials images
pygame_ess.load_essential_objects(caesar_cipher_objects, page_name, ['back', 'info'])

# Textfield
caesar_cipher_objects['plaintext'] = item(name='plaintext',
                                          type='textfield',
                                          meta=text_data(
                                              text='plaintext',
                                              font_type='Monaco.dfont',
                                              font_size=34,
                                              colour=pygame_ess.colour.black
                                              ),
                                          images=pygame_ess.load_images([page_name, 'plaintext']),
                                          frame=coord(
                                              325, 156, 
                                              632, 62, 
                                              307, 146
                                              ),
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
                                          images=pygame_ess.load_images([page_name, 'key']),
                                          frame=coord(
                                              325, 238, 
                                              160, 62, 
                                              307, 229
                                              ),
                                          runclass=textfield_event.run)

caesar_cipher_objects['alphabet'] = item(name='alphabet',
                                          type='textfield',
                                          meta=text_data(
                                              text='"ABCDEFGHIJKLMNOPQRSTUVWXYZ"',
                                              font_type='Monaco.dfont',
                                              font_size=34,
                                              colour=pygame_ess.colour.white
                                              ),
                                          images=pygame_ess.load_images([page_name, 'alphabet']),
                                          frame=coord(
                                              311, 403, 
                                              649, 47, 
                                              311, 403
                                              ),
                                          runclass='')

caesar_cipher_objects['replaced'] = item(name='replaced',
                                         type='textfield',
                                         meta=text_data(
                                                text='"ABCDEFGHIJKLMNOPQRSTUVWXYZ"',
                                                font_type='Monaco.dfont',
                                                font_size=34,
                                                colour=pygame_ess.colour.white
                                                ),
                                         images=pygame_ess.load_images([page_name, 'replaced']),
                                         frame=coord(
                                                311, 464, 
                                                649, 47, 
                                                311, 464
                                                ),
                                         runclass='')

caesar_cipher_objects['ciphertext'] = item(name='ciphertext',
                                           type='textfield',
                                           meta=text_data(
                                                text='ciphertext',
                                                font_type='Monaco.dfont',
                                                font_size=34,
                                                colour=pygame_ess.colour.black
                                                ),
                                           images=pygame_ess.load_images([page_name, 'ciphertext']),
                                           frame=coord(
                                                325, 574, 
                                                632, 62, 
                                                307, 564
                                                ),
                                           runclass='')


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
        textfield_event.update_textfield(caesar_cipher_window, caesar_cipher_objects['replaced'], False)
        textfield_event.update_textfield(caesar_cipher_window, caesar_cipher_objects['ciphertext'], False)

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
        textfield_event.update_textfield(caesar_cipher_window, caesar_cipher_objects['replaced'], False)
        textfield_event.update_textfield(caesar_cipher_window, caesar_cipher_objects['plaintext'], False)

        return plaintext
    
    def run():
        '''Display Caesar Cipher Page'''
        
        # Load the screen
        caesar_cipher.decrypt()
        logging.info('Loaded caesar cipher window...')
         
        while True:
            # Check for selection
            selection_result:dict = pygame_ess.selection_event(caesar_cipher_window, caesar_cipher_objects)

            # Quit program
            if selection_result['action_result'] == 'quit' or pygame_ess.buffer(caesar_cipher_window): 
                return 'quit'

            # Button press
            elif selection_result['object_type'] == 'button':
                # Go back to previous page
                if selection_result['action_result'] == 'back': return True
            
            # Textfield updated
            elif selection_result['object_type'] == 'textfield':
                # Update ciphertext
                caesar_cipher.encrypt()


#############
# Main loop #
#############
if __name__ == "__main__":
    pygame.init()
    # Run home screen
    caesar_cipher.run()

    # Done! Time to quit.
    pygame_ess.quit()
