######################################
# Import and initialize the librarys #
######################################
import pygame
from item_storage import *
from pygame_ess import pygame_ess
from textfield_event import textfield_event
from input_validation import validate


##################
# Initialization #
##################
pygame.init()
screen = pygame.display.set_mode((1024, 768))


#########################
# Variables declaration #
#########################
page_name:str = 'affine_cipher'
affine_cipher_objects: dict = dict()


##############################
# Load Affine Cipher objects #
##############################

# Load essentials images
pygame_ess.load_essential_objects(affine_cipher_objects, page_name, ['back', 'info'])

# Textfields
affine_cipher_objects['plaintext'] = item(name='plaintext',
                                          type='textfield',
                                          meta=text_data(
                                              text='plaintext',
                                              font_type='Monaco.dfont',
                                              font_size=34,
                                              colour=pygame_ess.colour.black
                                              ),
                                          images=pygame_ess.load_images([page_name, 'plaintext']),
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
                                images=pygame_ess.load_images([page_name, 'a']),
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
                                images=pygame_ess.load_images([page_name, 'b']),
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
                                              colour=pygame_ess.colour.black
                                              ),
                                          images=pygame_ess.load_images([page_name, 'ciphertext']),
                                          frame=coord(
                                              325, 535, 
                                              632, 62, 
                                              307, 526
                                              ),
                                          runclass='')


###################
# Generate window #
###################
affine_cipher_window:surface = surface(affine_cipher_objects)


######################
# Affine Cipher Page #
######################
class affine_cipher:
    '''Affine Cipher Page'''

    def encrypt() -> str:
        ''' Encrypt plaintext'''

        # Get plaintext and keys
        try:
            plaintext:str = str(affine_cipher_objects['plaintext'].meta.text)
            a:int = int(affine_cipher_objects['a'].meta.text)
            b:int = int(affine_cipher_objects['b'].meta.text)
        except:
            print('type error.')
            return

        # Variables
        alphabet = pygame_ess.alphabet

        # Calculate ciphertext
        ciphertext:str = ''
        for char in plaintext:
            if char.isalpha():
                cipherchar:str = alphabet[ (a * alphabet.find(char.upper()) + b) % 26 ]
                if char.islower(): cipherchar = cipherchar.lower()
                ciphertext += cipherchar

            else: ciphertext += char

        # Save back to ciphertext object
        affine_cipher_objects['ciphertext'].meta.text = ciphertext

        # Update screen
        textfield_event.update_textfield(affine_cipher_window, affine_cipher_objects['ciphertext'], False)

        return ciphertext

    def decrypt() -> str:
        ''' Decrypt cyphertext'''

        # Get cyphertext and keys
        try:
            cyphertext:str = str(affine_cipher_objects['plaintext'].meta.text)
            a:int = int(affine_cipher_objects['a'].meta.text)
            b:int = int(affine_cipher_objects['b'].meta.text)
        except:
            print('type error.')
            return

        # Variables
        alphabet = pygame_ess.alphabet

        # Calculate inverse A mod 26
        did_inverse_a = False
        for i in range(26):
            if (a * i) % 26 == 1: 
                did_inverse_a = True
                a = (a * i)
                break

        # If failed to convert    
        if not did_inverse_a: 
            print('Failed to calculate inverse A mod 26.')
            return

        # Calculate plaintext
        plaintext:str = ''
        for char in cyphertext:
            if char.isalpha():
                plainchar:str = alphabet[ (a * (alphabet.find(char.upper()) - b)) % 26 ]
                if char.islower(): plainchar = plainchar.lower()
                plaintext += plainchar

            else: plaintext += char
            

        # Save back to plaintext object
        affine_cipher_objects['plaintext'].meta.text = plaintext

        # Update screen
        textfield_event.update_textfield(affine_cipher_window, affine_cipher_objects['plaintext'], False)

        return plaintext


    def run():
        '''Display Affine Cipher Page'''

        # Load screen
        affine_cipher.decrypt()
        pygame_ess.load_screen(affine_cipher_window)

        while True:
            # Check for selection
            selection_result:dict = pygame_ess.selection_event(affine_cipher_window, affine_cipher_objects)

            # Quit program
            if selection_result['action_result'] == 'quit' or pygame_ess.buffer(affine_cipher_window): 
                return 'quit'

            # Button press
            elif selection_result['object_type'] == 'button':
                # Go back to previous page
                if selection_result['action_result'] == 'back': return True
            
            # Textfield updated
            elif selection_result['object_type'] == 'textfield':
                # Update ciphertext
                affine_cipher.encrypt()


#############
# Main loop #
#############
if __name__ == "__main__":
    # Run home screen
    affine_cipher.run()

    # Done! Time to quit.
    pygame_ess.quit()