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

atbash_cipher_objects['cyphertext'] = item(name='cyphertext',
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
class atbash_cipher:

    def algorithm():
        pass

    def run():
        # Load the screen
        pygame_ess.load_screen(screen, atbash_cipher_objects)
        atbash_cipher.algorithm()
         
        while True:
            # Check for selection
            selection_result = pygame_ess.selection(screen, atbash_cipher_objects)

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