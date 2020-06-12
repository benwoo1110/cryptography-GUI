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
page_name = 'polyalphabetic_substitution_cipher'
button_types = {'back':'back', 'info':''}
polyalphabetic_substitution_cipher_objects = dict()


##############################
# Load affine cipher objects #
##############################

# Load essentials images
pygame_ess.load_essential_objects(polyalphabetic_substitution_cipher_objects, page_name, ['back', 'info'])

# Textfield
polyalphabetic_substitution_cipher_objects['keyword'] = item(name='keyword',
                                          type='textfield',
                                          meta=text_data(
                                              text='KEYWORD',
                                              font_type='Monaco.dfont',
                                              font_size=34,
                                              colour=(0,0,0)
                                              ),
                                          images=pygame_ess.load_images([page_name, 'keyword']),
                                          frame=coord(
                                              325, 174, 
                                              632, 62, 
                                              307, 165
                                              ),
                                          runclass=textfield_event)

polyalphabetic_substitution_cipher_objects['plaintext'] = item(name='plaintext',
                                          type='textfield',
                                          meta=text_data(
                                              text='plaintext',
                                              font_type='Monaco.dfont',
                                              font_size=34,
                                              colour=(0,0,0)
                                              ),
                                          images=pygame_ess.load_images([page_name, 'plaintext']),
                                          frame=coord(
                                              325, 255, 
                                              632, 62, 
                                              307, 248
                                              ),
                                          runclass=textfield_event)

polyalphabetic_substitution_cipher_objects['text'] = item(name='text',
                                          type='textfield',
                                          meta=text_data(
                                              text='text',
                                              font_type='Monaco.dfont',
                                              font_size=34,
                                              colour=(255,255,255)
                                              ),
                                          images=pygame_ess.load_images([page_name, 'text']),
                                          frame=coord(
                                              325, 381, 
                                              632, 62, 
                                              325, 381
                                              ),
                                          runclass='')

polyalphabetic_substitution_cipher_objects['key'] = item(name='key',
                                          type='textfield',
                                          meta=text_data(
                                              text='key',
                                              font_type='Monaco.dfont',
                                              font_size=34,
                                              colour=(255,255,255)
                                              ),
                                          images=pygame_ess.load_images([page_name, 'key']),
                                          frame=coord(
                                              325, 437, 
                                              632, 62, 
                                              307, 437
                                              ),
                                          runclass='')

polyalphabetic_substitution_cipher_objects['ciphertext'] = item(name='ciphertext',
                                          type='textfield',
                                          meta=text_data(
                                              text='ciphertext',
                                              font_type='Monaco.dfont',
                                              font_size=34,
                                              colour=(0,0,0)
                                              ),
                                          images=pygame_ess.load_images([page_name, 'ciphertext']),
                                          frame=coord(
                                              325, 572, 
                                              632, 62, 
                                              307, 564
                                              ),
                                          runclass='')


###########################################
# Polyalphabetic Substitution Cipher Page #
###########################################
class polyalphabetic_substitution_cipher:
    '''Polyalphabetic Substitution Cipher Page'''

    def encrypt():
        ''' Encrypt plaintext'''

        # Get keyword and plaintext
        keyword = polyalphabetic_substitution_cipher_objects['keyword'].meta.text
        plaintext = polyalphabetic_substitution_cipher_objects['plaintext'].meta.text

        # Variables
        alphabet = alphabet = pygame_ess.alphabet
        
        # Update text
        polyalphabetic_substitution_cipher_objects['text'].meta.text = plaintext

        # Generate key
        plaintext_length = len(plaintext)
        keyword_length = len(keyword)
        key = keyword.upper() * (plaintext_length//keyword_length) + keyword.upper()[:plaintext_length%keyword_length]

        # Stores key
        polyalphabetic_substitution_cipher_objects['key'].meta.text = key

        # Calculate ciphertext
        ciphertext = ''
        for char in range(plaintext_length):
            if plaintext[char].isalpha():
                cipherchar = alphabet[ ( alphabet.find(plaintext[char].upper()) + alphabet.find(key[char].upper()) ) % 26 ]
                if plaintext[char].islower(): cipherchar = cipherchar.lower()
                ciphertext += cipherchar

            else: ciphertext += plaintext[char]

        # Stores ciphertext
        polyalphabetic_substitution_cipher_objects['ciphertext'].meta.text = ciphertext

        # Output to screen
        for text in ['text', 'key', 'ciphertext']:
            textfield_event.update_textfield(polyalphabetic_substitution_cipher_objects[text], False)

        return ciphertext

    def run():
        '''Polyalphabetic Substitution Cipher Page'''

        # Load screen
        pygame_ess.load_screen(polyalphabetic_substitution_cipher_objects)
        polyalphabetic_substitution_cipher.algorithm()

        while True:
            # Check for selection
            selection_result = pygame_ess.selection_event(polyalphabetic_substitution_cipher_objects)

            # Load back current screen
            if selection_result['action_result'] == True: pygame_ess.load_screen(polyalphabetic_substitution_cipher_objects)
            
            # Button press
            elif selection_result['object_type'] == 'button':
                # Go back to previous page
                if selection_result['action_result'] == 'back': return True
            
            # Textfield updated
            elif selection_result['object_type'] == 'textfield':
                # Update ciphertext
                polyalphabetic_substitution_cipher.encrypt()

            # Quit program
            elif selection_result['action_result'] == 'quit' or pygame_ess.buffer(): return 'quit'



#############
# Main loop #
#############
if __name__ == "__main__":
    # Run home screen
    polyalphabetic_substitution_cipher.run()

    # Done! Time to quit.
    pygame_ess.quit()