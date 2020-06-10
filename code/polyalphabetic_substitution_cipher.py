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
page_name = 'polyalphabetic_substitution_cipher'
button_types = {'back':'back', 'info':''}
polyalphabetic_substitution_cipher_objects = dict()


##
## Load home screen objects

# background image
polyalphabetic_substitution_cipher_objects['background'] = item(name='cryptography background',
                                           type='background', 
                                           images=pygame_ess.load_images([page_name]))

# Buttons
for button_type in button_types.keys():
    polyalphabetic_substitution_cipher_objects[button_type] = item(name=button_type,
                                              type='button',
                                              images=pygame_ess.load_images([page_name, button_type]),
                                              frame=coord(
                                                  47 + 766 * list(button_types.keys()).index(button_type), 28, 
                                                  162, 67, 
                                                  (48 + 766) * list(button_types.keys()).index(button_type), 0
                                                  ),
                                              runclass=button_types[button_type])

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
                                          type='text',
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
                                          type='text',
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

polyalphabetic_substitution_cipher_objects['cyphertext'] = item(name='cyphertext',
                                          type='text',
                                          meta=text_data(
                                              text='cyphertext',
                                              font_type='Monaco.dfont',
                                              font_size=34,
                                              colour=(0,0,0)
                                              ),
                                          images=pygame_ess.load_images([page_name, 'cyphertext']),
                                          frame=coord(
                                              325, 572, 
                                              632, 62, 
                                              307, 564
                                              ),
                                          runclass='')



##
## 
class polyalphabetic_substitution_cipher:

    def algorithm():
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        # Get keyword and plaintext
        keyword = polyalphabetic_substitution_cipher_objects['keyword'].meta.text
        plaintext = polyalphabetic_substitution_cipher_objects['plaintext'].meta.text

        # Update text
        polyalphabetic_substitution_cipher_objects['text'].meta.text = plaintext

        # Generate key
        plaintext_length = len(plaintext)
        keyword_length = len(keyword)
        key = keyword.upper() * (plaintext_length//keyword_length) + keyword.upper()[:plaintext_length%keyword_length]

        polyalphabetic_substitution_cipher_objects['key'].meta.text = key

        # Calculate cyphertext
        cyphertext = ''
        for char in range(plaintext_length):
            if plaintext[char].isalpha():
                cypherchar = alphabet[ ( alphabet.find(plaintext[char].upper()) + alphabet.find(key[char].upper()) ) % 26 ]
                if plaintext[char].islower(): cypherchar = cypherchar.lower()
                cyphertext += cypherchar

            else: cyphertext += plaintext[char]

        polyalphabetic_substitution_cipher_objects['cyphertext'].meta.text = cyphertext

        # Output to screen
        for text in ['text', 'key', 'cyphertext']:
            textfield_event.update_textfield(screen, polyalphabetic_substitution_cipher_objects[text], False)

        return cyphertext

    def run():
        # Load screen
        pygame_ess.load_screen(screen, polyalphabetic_substitution_cipher_objects)
        polyalphabetic_substitution_cipher.algorithm()

        while True:
            # Check for selection
            selection_result = pygame_ess.selection(screen, polyalphabetic_substitution_cipher_objects)
            selection_result_key, selection_result_value = list(selection_result.keys())[0], list(selection_result.values())[0]
            
            # Button pressed
            if selection_result_key == 'button':
                if selection_result_value == True: pygame_ess.load_screen(screen, polyalphabetic_substitution_cipher_objects)
                elif selection_result_value == 'back': return True
            
            # Testfield pressed
            elif selection_result_key == 'textfield':
                polyalphabetic_substitution_cipher.algorithm()

            if pygame_ess.buffer(): break


##
## Main loop
if __name__ == "__main__":
    # Run home screen
    polyalphabetic_substitution_cipher.run()

    # Done! Time to quit.
    print('Exiting program...')
    pygame.quit()