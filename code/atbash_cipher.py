######################################
# Import and initialize the librarys #
######################################
import pygame
from item_storage import *
from pygame_ess import pygame_ess
from textfield_event import textfield_event


##################
# Initialization #
##################
pygame.init()

# Set up the drawing window
window_size = (1024, 768)
screen = pygame.display.set_mode((1024, 768))
window = pygame.surface.Surface((window_size))


#########################
# Variables declaration #
#########################
page_name = 'atbash_cipher'
atbash_cipher_objects = dict()


##############################
# Load affine cipher objects #
##############################

# background image
pygame_ess.load_essential_objects(atbash_cipher_objects, page_name, ['back', 'info'])

# Textfield
atbash_cipher_objects['plaintext'] = item(name='plaintext',
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

atbash_cipher_objects['ciphertext'] = item(name='ciphertext',
                                          type='textfield',
                                          meta=text_data(
                                              text='ciphertext',
                                              font_type='Monaco.dfont',
                                              font_size=34,
                                              colour=pygame_ess.colour.black
                                              ),
                                          images=pygame_ess.load_images([page_name, 'ciphertext']),
                                          frame=coord(
                                              325, 540, 
                                              632, 62, 
                                              307, 533
                                              ),
                                          runclass='')


######################
# Atbash Cipher Page #
######################
class atbash_cipher:
    '''Atbash Cipher Page'''

    def encrypt():
        ''' Encrypt plaintext'''

        # Get plaintext
        plaintext = atbash_cipher_objects['plaintext'].meta.text

        # Variables
        alphabet = pygame_ess.alphabet
        replace = alphabet[::-1]

        # Calculate ciphertext
        ciphertext = ''
        for char in plaintext:
            if char.isalpha():
                cipherchar = replace[alphabet.find(char.upper())]
                if char.islower(): cipherchar = cipherchar.lower()
                ciphertext += cipherchar

            else: ciphertext += char

        # Output to screen
        atbash_cipher_objects['ciphertext'].meta.text = ciphertext
        textfield_event.update_textfield(atbash_cipher_objects['ciphertext'], False)

        return ciphertext

    def run():
        '''Display Atbash Cipher Page'''

        # Load the screen
        pygame_ess.load_screen(atbash_cipher_objects)
        atbash_cipher.encrypt()
         
        while True:
            # Check for selection
            selection_result = pygame_ess.selection_event(atbash_cipher_objects)

            # Load back current screen
            if selection_result['action_result'] == True: pygame_ess.load_screen(atbash_cipher_objects)
            
            # Button press
            elif selection_result['object_type'] == 'button':
                # Go back to previous page
                if selection_result['action_result'] == 'back': return True
            
            # Textfield updated
            elif selection_result['object_type'] == 'textfield':
                # Update ciphertext
                atbash_cipher.encrypt()

            # Quit program
            elif selection_result['action_result'] == 'quit' or pygame_ess.buffer(): return 'quit'


#############
# Main loop #
#############
if __name__ == "__main__":
    # Run home screen
    atbash_cipher.run()

    # Done! Time to quit.
    pygame_ess.quit()