##
## Import and initialize the librarys
import pygame
from item_storage import *
from pygame_ess import pygame_ess
from textfield_event import textfield_event
import random


##
## Initialization
pygame.init()

# Set up the drawing window
window_size = (1024, 768)
screen = pygame.display.set_mode((1024, 768))
window = pygame.surface.Surface((window_size))


##
## Variables
page_name = 'monoalphabetic_subsitution_cipher'
button_types = {'back':'back', 'info':''}
monoalphabetic_subsitution_cipher_objects = dict()


##
## Load home screen objects

# background image
monoalphabetic_subsitution_cipher_objects['background'] = item(name='cryptography background',
                                           type='background', 
                                           images=pygame_ess.load_images([page_name]))

# Buttons
for button_type in button_types.keys():
    monoalphabetic_subsitution_cipher_objects[button_type] = item(name=button_type,
                                              type='button',
                                              images=pygame_ess.load_images([page_name, button_type]),
                                              frame=coord(
                                                  47 + 766 * list(button_types.keys()).index(button_type), 28, 
                                                  162, 67, 
                                                  (48 + 766) * list(button_types.keys()).index(button_type), 0
                                                  ),
                                              runclass=button_types[button_type])

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
                                              colour=(0,0,0)
                                              ),
                                          images=pygame_ess.load_images([page_name, 'plaintext']),
                                          frame=coord(
                                              325, 172, 
                                              632, 62, 
                                              307, 165
                                              ),
                                          runclass=textfield_event)

monoalphabetic_subsitution_cipher_objects['alphabet'] = item(name='alphabet',
                                          type='text',
                                          meta=text_data(
                                              text='"ABCDEFGHIJKLMNOPQRSTUVWXYZ"',
                                              font_type='Monaco.dfont',
                                              font_size=34,
                                              colour=(255,255,255)
                                              ),
                                          images=pygame_ess.load_images([page_name, 'alphabet']),
                                          frame=coord(
                                              325, 314, 
                                              632, 62, 
                                              325, 314
                                              ),
                                          runclass='')

monoalphabetic_subsitution_cipher_objects['key'] = item(name='key',
                                          type='text',
                                          meta=text_data(
                                              text='"ABCDEFGHIJKLMNOPQRSTUVWXYZ"',
                                              font_type='Monaco.dfont',
                                              font_size=34,
                                              colour=(0,0,0)
                                              ),
                                          images=pygame_ess.load_images([page_name, 'key']),
                                          frame=coord(
                                              325, 384, 
                                              632, 62, 
                                              307, 375
                                              ),
                                          runclass='')

monoalphabetic_subsitution_cipher_objects['cyphertext'] = item(name='cyphertext',
                                          type='text',
                                          meta=text_data(
                                              text='cyphertext',
                                              font_type='Monaco.dfont',
                                              font_size=34,
                                              colour=(0,0,0)
                                              ),
                                          images=pygame_ess.load_images([page_name, 'cyphertext']),
                                          frame=coord(
                                              325, 609, 
                                              632, 62, 
                                              307, 601
                                              ),
                                          runclass='')


##
## 
class monoalphabetic_subsitution_cipher:

    def shuffle():
        # Shuffle the key
        shuffled_alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        random.shuffle(shuffled_alphabet)
        monoalphabetic_subsitution_cipher_objects['key'].meta.text = '"' +  ''.join(shuffled_alphabet) + '"'

        # Update key text        
        textfield_event.update_textfield(screen, monoalphabetic_subsitution_cipher_objects['key'], selected=False)
        
        # Update the cyphertext
        monoalphabetic_subsitution_cipher.algorithm()

    def algorithm():
        # Get plaintext and key
        plaintext = monoalphabetic_subsitution_cipher_objects['plaintext'].meta.text
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        key = monoalphabetic_subsitution_cipher_objects['key'].meta.text[1:-1]

        # Get cyphertext
        cyphertext = ''
        for char in plaintext:
            if char.isalpha():
                cypherchar = key[alphabet.index(char.upper())]
                if char.islower(): cypherchar = cypherchar.lower()

                cyphertext += cypherchar
                
            else: cyphertext += char

        monoalphabetic_subsitution_cipher_objects['cyphertext'].meta.text = cyphertext

        # Update screen
        textfield_event.update_textfield(screen, monoalphabetic_subsitution_cipher_objects['cyphertext'], False)
    
    def run():
        # Load screen
        pygame_ess.load_screen(screen, monoalphabetic_subsitution_cipher_objects)
        monoalphabetic_subsitution_cipher.shuffle()
        
        # Check for selection
        while True:
            selection_result = pygame_ess.selection(screen, monoalphabetic_subsitution_cipher_objects)
            selection_result_key, selection_result_value = list(selection_result.keys())[0], list(selection_result.values())[0]
            
            
            if selection_result_key == 'button': 
                if selection_result_value == True: pygame_ess.load_screen(screen, monoalphabetic_subsitution_cipher_objects)
                if selection_result_value == 'shuffle': monoalphabetic_subsitution_cipher.shuffle()
                elif selection_result_value == 'back': break

            elif selection_result_key == 'textfield': monoalphabetic_subsitution_cipher.algorithm()


            if pygame_ess.buffer(): break


##
## Main loop
if __name__ == "__main__":
    # Run home screen
    monoalphabetic_subsitution_cipher.run()

    # Done! Time to quit.
    print('Exiting program...')
    pygame.quit()