##
## Import and initialize the librarys
import pygame
from pygame_ess import pygame_ess
from item_storage import *
from caesar_cipher import caesar_cipher
from monoalphabetic_cipher import monoalphabetic_cipher
from homophonic_substitution_cipher import homophonic_substitution_cipher
from polygram_subsitution_cipher import polygram_subsitution_cipher
from polyalphabetic_substitution_cipher import polyalphabetic_substitution_cipher


##
## Initialization
pygame.init()

# Set up the drawing window
window_size = (1024, 768)
screen = pygame.display.set_mode((1024, 768))
window = pygame.surface.Surface((window_size))
pygame.display.set_caption("Cryptography")


##
## Variables
page_name = 'cryptography'

'''
cipher_types = {'caesar_cipher':caesar_cipher, 
                'monoalphabetic_cipher':monoalphabetic_cipher, 
                'homophonic_substitution_cipher':homophonic_substitution_cipher,
                'polygram_subsitution_cipher':polygram_subsitution_cipher, 
                'polyalphabetic_substitution_cipher':polyalphabetic_substitution_cipher}
'''

cipher_types = {'caesar_cipher':caesar_cipher, 
                'monoalphabetic_cipher':'monoalphabetic_cipher', 
                'homophonic_substitution_cipher':'homophonic_substitution_cipher',
                'polygram_subsitution_cipher':'polygram_subsitution_cipher', 
                'polyalphabetic_substitution_cipher':'polyalphabetic_substitution_cipher'}

cryptography_objects = dict()


##
## Load home screen objects

# background image
cryptography_objects['background'] = item(name='cryptography background',
                                          type='background', 
                                          images=pygame_ess.load_images([page_name]))

# cipher list
for cipher_type in cipher_types.keys():
    cipher_type_y_coord = 112 + list(cipher_types.keys()).index(cipher_type) * 106
    cryptography_objects[cipher_type] = item(name=cipher_type,
                                             type='button',
                                             images=pygame_ess.load_images([page_name, cipher_type]),
                                             frame=coord(47, cipher_type_y_coord, 929, 86, 0, cipher_type_y_coord),
                                             runclass=cipher_types[cipher_type])


##
##
class cryptography:
    def run():
        # Load the screen
        pygame_ess.load_screen(screen, cryptography_objects)

        while True:
            # Check for selection
            selection_result = pygame_ess.selection(screen, cryptography_objects)
            selection_result_key, selection_result_value = list(selection_result.keys())[0], list(selection_result.values())[0]
            
            if selection_result_key == 'button':
                if selection_result_value == True: pygame_ess.load_screen(screen, cryptography_objects)
            
            # End program
            if pygame_ess.buffer(): return True


##
## Main loop
if __name__ == "__main__":
    # Run home screen
    cryptography.run()

    # Done! Time to quit.
    print('Exiting progam...')
    pygame.quit()

