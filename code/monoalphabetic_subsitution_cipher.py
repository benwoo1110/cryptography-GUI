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
pygame_ess.load_essential_objects(monoalphabetic_subsitution_cipher_objects, page_name)

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

monoalphabetic_subsitution_cipher_objects['ciphertext'] = item(name='ciphertext',
                                          type='text',
                                          meta=text_data(
                                              text='ciphertext',
                                              font_type='Monaco.dfont',
                                              font_size=34,
                                              colour=(0,0,0)
                                              ),
                                          images=pygame_ess.load_images([page_name, 'ciphertext']),
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
        
        # Update the ciphertext
        monoalphabetic_subsitution_cipher.algorithm()

    def algorithm():
        # Get plaintext and key
        plaintext = monoalphabetic_subsitution_cipher_objects['plaintext'].meta.text
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        key = monoalphabetic_subsitution_cipher_objects['key'].meta.text[1:-1]

        # Get ciphertext
        ciphertext = ''
        for char in plaintext:
            if char.isalpha():
                cipherchar = key[alphabet.index(char.upper())]
                if char.islower(): cipherchar = cipherchar.lower()

                ciphertext += cipherchar
                
            else: ciphertext += char

        monoalphabetic_subsitution_cipher_objects['ciphertext'].meta.text = ciphertext

        # Update screen
        textfield_event.update_textfield(screen, monoalphabetic_subsitution_cipher_objects['ciphertext'], False)
    
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