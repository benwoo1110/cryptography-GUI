######################################
# Import and initialize the librarys #
######################################
import pygame
from item_storage import *
from pygame_ess import pygame_ess
from textfield_event import textfield_event
import random


##################
# Initialization #
##################
pygame.init()
screen = pygame.display.set_mode((1024, 768))

#########################
# Variables declaration #
#########################
page_name:str = 'monoalphabetic_subsitution_cipher'
button_types:dict = {'back':'back', 'info':''}
monoalphabetic_subsitution_cipher_objects:dict = dict()


##############################
# Load affine cipher objects #
##############################

# Load essentials images
pygame_ess.load_essential_objects(monoalphabetic_subsitution_cipher_objects, page_name, ['back', 'info'])

# Button
monoalphabetic_subsitution_cipher_objects['shuffle'] = item(name='shuffle',
                                              type='button',
                                              images=pygame_ess.load_images([page_name, 'shuffle']),
                                              frame=coord(
                                                  738, 459, 
                                                  199, 56, 
                                                  738, 459
                                                  ),
                                              runclass='shuffle')

# Textfield
monoalphabetic_subsitution_cipher_objects['plaintext'] = item(name='plaintext',
                                          type='textfield',
                                          meta=text_data(
                                              text='plaintext',
                                              font_type='Monaco.dfont',
                                              font_size=34,
                                              colour=pygame_ess.colour.black
                                              ),
                                          images=pygame_ess.load_images([page_name, 'plaintext']),
                                          frame=coord(
                                              325, 172, 
                                              632, 62, 
                                              307, 165
                                              ),
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
                                              325, 314
                                              ),
                                          runclass='')

monoalphabetic_subsitution_cipher_objects['key'] = item(name='key',
                                          type='textfield',
                                          meta=text_data(
                                              text='"ABCDEFGHIJKLMNOPQRSTUVWXYZ"',
                                              font_type='Monaco.dfont',
                                              font_size=34,
                                              colour=pygame_ess.colour.black
                                              ),
                                          images=pygame_ess.load_images([page_name, 'key']),
                                          frame=coord(
                                              325, 384, 
                                              632, 62, 
                                              307, 375
                                              ),
                                          runclass='')

monoalphabetic_subsitution_cipher_objects['ciphertext'] = item(name='ciphertext',
                                          type='textfield',
                                          meta=text_data(
                                              text='ciphertext',
                                              font_type='Monaco.dfont',
                                              font_size=34,
                                              colour=pygame_ess.colour.black
                                              ),
                                          images=pygame_ess.load_images([page_name, 'ciphertext']),
                                          frame=coord(
                                              325, 609, 
                                              632, 62, 
                                              307, 601
                                              ),
                                          runclass='')


###################
# Generate window #
###################
monoalphabetic_subsitution_cipher_window:surface = surface(monoalphabetic_subsitution_cipher_objects)


##########################################
# Monoalphabetic Subsitution Cipher Page #
##########################################
class monoalphabetic_subsitution_cipher:
    '''Monoalphabetic Subsitution Cipher Page'''

    def shuffle():
        ''' Encrypt plaintext'''

        # Shuffle the key
        shuffled_alphabet:list = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        random.shuffle(shuffled_alphabet)
        monoalphabetic_subsitution_cipher_objects['key'].meta.text = '"' +  ''.join(shuffled_alphabet) + '"'

        # Update key text        
        textfield_event.update_textfield(monoalphabetic_subsitution_cipher_window, monoalphabetic_subsitution_cipher_objects['key'], selected=False)
        
        # Update the ciphertext
        monoalphabetic_subsitution_cipher.encrypt()

    def encrypt() -> str:
        # Get plaintext and key
        plaintext = monoalphabetic_subsitution_cipher_objects['plaintext'].meta.text
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
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
    
    def run():
        '''Display Monoalphabetic Subsitution Cipher Page'''

        # Load screen
        pygame_ess.load_screen(monoalphabetic_subsitution_cipher_window)
        monoalphabetic_subsitution_cipher.shuffle()

        while True:
            # Check for selection
            selection_result:dict = pygame_ess.selection_event(monoalphabetic_subsitution_cipher_window, monoalphabetic_subsitution_cipher_objects)

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
                # Update ciphertext
                monoalphabetic_subsitution_cipher.encrypt()


#############
# Main loop #
#############
if __name__ == "__main__":
    # Run home screen
    monoalphabetic_subsitution_cipher.run()

    # Done! Time to quit.
    pygame_ess.quit()