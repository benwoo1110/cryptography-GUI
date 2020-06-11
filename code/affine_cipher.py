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
page_name = 'affine_cipher'
affine_cipher_objects = dict()


##
## Load home screen objects
pygame_ess.load_essential_objects(affine_cipher_objects, page_name)

# Textfields
affine_cipher_objects['plaintext'] = item(name='plaintext',
                                          type='textfield',
                                          meta=text_data(
                                              text='plaintext',
                                              font_type='Monaco.dfont',
                                              font_size=34,
                                              colour=(0,0,0)
                                              ),
                                          images=pygame_ess.load_images([page_name, 'plaintext']),
                                          frame=coord(
                                              325, 158, 
                                              632, 62, 
                                              307, 150
                                              ),
                                          runclass=textfield_event)

affine_cipher_objects['a'] = item(name='a',
                                          type='textfield',
                                          meta=text_data(
                                              text='1',
                                              font_type='Monaco.dfont',
                                              font_size=34,
                                              colour=(0,0,0)
                                              ),
                                          images=pygame_ess.load_images([page_name, 'a']),
                                          frame=coord(
                                              325, 248, 
                                              160, 62, 
                                              307, 238
                                              ),
                                          runclass=textfield_event)     

affine_cipher_objects['b'] = item(name='b',
                                          type='textfield',
                                          meta=text_data(
                                              text='2',
                                              font_type='Monaco.dfont',
                                              font_size=34,
                                              colour=(0,0,0)
                                              ),
                                          images=pygame_ess.load_images([page_name, 'b']),
                                          frame=coord(
                                              569, 247, 
                                              160, 62, 
                                              551, 238
                                              ),
                                          runclass=textfield_event)   

affine_cipher_objects['ciphertext'] = item(name='ciphertext',
                                          type='text',
                                          meta=text_data(
                                              text='ciphertext',
                                              font_type='Monaco.dfont',
                                              font_size=34,
                                              colour=(0,0,0)
                                              ),
                                          images=pygame_ess.load_images([page_name, 'ciphertext']),
                                          frame=coord(
                                              325, 535, 
                                              632, 62, 
                                              307, 526
                                              ),
                                          runclass='')


##
##
class affine_cipher:

    def algorithm():
        # Get plaintext and keys
        try:
            plaintext = str(affine_cipher_objects['plaintext'].meta.text)
            a = int(affine_cipher_objects['a'].meta.text)
            b = int(affine_cipher_objects['b'].meta.text)
        except:
            print('type error.')
            return

        # Variable
        alphabet = 'ABCDDEFHIJKLMNOPQRSTUVWXYZ'

        # Get ciphertext
        ciphertext = ''
        for char in plaintext:
            if char.isalpha():
                cipherchar = alphabet[ (a * alphabet.find(char.upper()) + b) % 26 ]
                if char.islower(): cipherchar = cipherchar.lower()
                ciphertext += cipherchar

            else: ciphertext += char

        affine_cipher_objects['ciphertext'].meta.text = ciphertext

        # Update screen
        textfield_event.update_textfield(screen, affine_cipher_objects['ciphertext'], False)

        return ciphertext

    def run():
        # Load screen
        pygame_ess.load_screen(screen, affine_cipher_objects)
        affine_cipher.algorithm()

        while True:
            # Check for selection
            selection_result = pygame_ess.selection(screen, affine_cipher_objects)
            selection_result_key, selection_result_value = list(selection_result.keys())[0], list(selection_result.values())[0]
            
            # Button pressed
            if selection_result_key == 'button':
                if selection_result_value == True: pygame_ess.load_screen(screen, affine_cipher_objects)
                elif selection_result_value == 'back': return True
            
            # Testfield pressed
            elif selection_result_key == 'textfield':
                # Update ciphertext
                affine_cipher.algorithm()

            if pygame_ess.buffer(): return True


##
## Main loop
if __name__ == "__main__":
    # Run home screen
    affine_cipher.run()

    # Done! Time to quit.
    print('Exiting program...')
    pygame.quit()