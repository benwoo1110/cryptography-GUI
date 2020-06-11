##
## Import and initialize the librarys
import pygame
from item_storage import *
from pygame_ess import pygame_ess
from textfield_event import textfield_event

##
## Initialization
pygame.init()

# Set up the drawing window
window_size = (1024, 768)
screen = pygame.display.set_mode((1024, 768))
window = pygame.surface.Surface((window_size))


##
## Variables
page_name = 'atbash_cipher'
atbash_cipher_objects = dict()


##
## Load home screen objects

# background image
pygame_ess.load_essential_objects(atbash_cipher_objects, page_name)

# Textfield
atbash_cipher_objects['plaintext'] = item(name='plaintext',
                                          type='textfield',
                                          meta=text_data(
                                              text='plaintext',
                                              font_type='Monaco.dfont',
                                              font_size=34,
                                              colour=(0,0,0)
                                              ),
                                          images=pygame_ess.load_images([page_name, 'plaintext']),
                                          frame=coord(
                                              325, 156, 
                                              632, 62, 
                                              307, 146
                                              ),
                                          runclass=textfield_event)

atbash_cipher_objects['ciphertext'] = item(name='ciphertext',
                                          type='text',
                                          meta=text_data(
                                              text='ciphertext',
                                              font_type='Monaco.dfont',
                                              font_size=34,
                                              colour=(0,0,0)
                                              ),
                                          images=pygame_ess.load_images([page_name, 'ciphertext']),
                                          frame=coord(
                                              325, 540, 
                                              632, 62, 
                                              307, 533
                                              ),
                                          runclass='')


##
##
class atbash_cipher:

    def algorithm():
        # Get plaintext
        plaintext = atbash_cipher_objects['plaintext'].meta.text

        # Variables
        alphabet = 'ABCDDEFHIJKLMNOPQRSTUVWXYZ'
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
        textfield_event.update_textfield(screen, atbash_cipher_objects['ciphertext'], False)

        return ciphertext

    def run():
        # Load the screen
        pygame_ess.load_screen(screen, atbash_cipher_objects)
        atbash_cipher.algorithm()
         
        while True:
            # Check for selection
            selection_result = pygame_ess.selection(screen, atbash_cipher_objects)
            selection_result_key, selection_result_value = list(selection_result.keys())[0], list(selection_result.values())[0]
            
            # Button pressed
            if selection_result_key == 'button':
                if selection_result_value == True: pygame_ess.load_screen(screen, atbash_cipher_objects)
                elif selection_result_value == 'back': return True
            
            # Testfield pressed
            elif selection_result_key == 'textfield':
                # Update ciphertext
                atbash_cipher.algorithm()

            # Kill page
            if pygame_ess.buffer(): return True


##
## Main loop
if __name__ == "__main__":
    # Run home screen
    atbash_cipher.run()

    # Done! Time to quit.
    print('Exiting program...')
    pygame.quit()