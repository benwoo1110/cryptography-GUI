######################################
# Import and initialize the librarys #
######################################
import logging
import pygame
from item_storage import *
from pygame_ess import pygame_ess
from mode import Mode
from textfield_event import textfield_event


##################
# Initialization #
##################
logging.info('Loading polyalphabetic subsitution cipher...')
screen = pygame.display.set_mode((1024, 768))


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
pygame_ess.load_essential_objects(polyalphabetic_substitution_cipher_objects, page_name, ['back', 'info'])

# Textfield
polyalphabetic_substitution_cipher_objects['keyword'] = item(name='keyword',
                                          type='textfield',
                                          meta=text_data(
                                              text='KEYWORD',
                                              font_type='Monaco.dfont',
                                              font_size=34,
                                              colour=pygame_ess.colour.black
                                              ),
                                          images=pygame_ess.load_images([page_name, 'keyword']),
                                          frame=coord(
                                              325, 174, 
                                              632, 62, 
                                              307, 165),
                                          runclass=textfield_event.run)

polyalphabetic_substitution_cipher_objects['plaintext'] = item(name='plaintext',
                                          type='textfield',
                                          meta=text_data(
                                              text='plaintext',
                                              font_type='Monaco.dfont',
                                              font_size=34,
                                              colour=pygame_ess.colour.black
                                              ),
                                          images=pygame_ess.load_images([page_name, 'plaintext']),
                                          frame=coord(
                                              325, 255, 
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
                                          images=pygame_ess.load_images([page_name, 'text']),
                                          frame=coord(
                                              325, 381, 
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
                                          images=pygame_ess.load_images([page_name, 'key']),
                                          frame=coord(
                                              325, 437, 
                                              632, 62, 
                                              307, 437),)

polyalphabetic_substitution_cipher_objects['ciphertext'] = item(name='ciphertext',
                                          type='textfield',
                                          meta=text_data(
                                              text='ciphertext',
                                              font_type='Monaco.dfont',
                                              font_size=34,
                                              colour=pygame_ess.colour.black
                                              ),
                                          images=pygame_ess.load_images([page_name, 'ciphertext']),
                                          frame=coord(
                                              325, 572, 
                                              632, 62, 
                                              307, 564),)


###################
# Generate window #
###################
logging.debug('Initialising polyalphabetic subsitution window...')
polyalphabetic_substitution_cipher_window:surface = surface(polyalphabetic_substitution_cipher_objects, name=page_name)


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
        for text in ['text', 'key', 'ciphertext']:
            textfield_event.update_textfield(polyalphabetic_substitution_cipher_window, polyalphabetic_substitution_cipher_objects[text], False)

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
            
            else: plaintext += plaintext[char]

        # Stores ciphertext
        polyalphabetic_substitution_cipher_objects['plaintext'].meta.text = plaintext

        # Update text
        polyalphabetic_substitution_cipher_objects['text'].meta.text = plaintext
        print(polyalphabetic_substitution_cipher_objects['text'].meta.text)

        # Output to screen
        for text in ['text', 'key', 'plaintext']:
            textfield_event.update_textfield(polyalphabetic_substitution_cipher_window, polyalphabetic_substitution_cipher_objects[text], False)

        return plaintext

    def run():
        '''Polyalphabetic Substitution Cipher Page'''

        # Load mode button
        mode.set_mode(polyalphabetic_substitution_cipher_window, polyalphabetic_substitution_cipher_objects)     
        # Load screen
        polyalphabetic_substitution_cipher.encrypt()
        logging.info('Loaded polyalphabetic subsitution window.')

        while True:
            # Check for selection
            selection_result:dict = pygame_ess.selection_event(polyalphabetic_substitution_cipher_window, polyalphabetic_substitution_cipher_objects)

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