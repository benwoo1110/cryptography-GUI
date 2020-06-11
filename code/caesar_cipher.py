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
page_name = 'caesar_cipher'
caesar_cipher_objects = dict()


##
## Load home screen objects
pygame_ess.load_essential_objects(caesar_cipher_objects, page_name)

# Textfield
caesar_cipher_objects['plaintext'] = item(name='plaintext',
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

caesar_cipher_objects['key'] = item(name='key',
                                          type='textfield',
                                          meta=text_data(
                                              text='1',
                                              font_type='Monaco.dfont',
                                              font_size=34,
                                              colour=(0,0,0)
                                              ),
                                          images=pygame_ess.load_images([page_name, 'key']),
                                          frame=coord(
                                              325, 238, 
                                              160, 62, 
                                              307, 229
                                              ),
                                          runclass=textfield_event)

caesar_cipher_objects['alphabet'] = item(name='alphabet',
                                          type='text',
                                          meta=text_data(
                                              text='"ABCDEFGHIJKLMNOPQRSTUVWXYZ"',
                                              font_type='Monaco.dfont',
                                              font_size=34,
                                              colour=(255,255,255)
                                              ),
                                          images=pygame_ess.load_images([page_name, 'alphabet']),
                                          frame=coord(
                                              311, 403, 
                                              649, 47, 
                                              311, 403
                                              ),
                                          runclass='')

caesar_cipher_objects['replaced'] = item(name='replaced',
                                          type='text',
                                          meta=text_data(
                                              text='"ABCDEFGHIJKLMNOPQRSTUVWXYZ"',
                                              font_type='Monaco.dfont',
                                              font_size=34,
                                              colour=(255,255,255)
                                              ),
                                          images=pygame_ess.load_images([page_name, 'replaced']),
                                          frame=coord(
                                              311, 464, 
                                              649, 47, 
                                              311, 464
                                              ),
                                          runclass='')

caesar_cipher_objects['ciphertext'] = item(name='ciphertext',
                                          type='text',
                                          meta=text_data(
                                              text='ciphertext',
                                              font_type='Monaco.dfont',
                                              font_size=34,
                                              colour=(0,0,0)
                                              ),
                                          images=pygame_ess.load_images([page_name, 'ciphertext']),
                                          frame=coord(
                                              325, 574, 
                                              632, 62, 
                                              307, 564
                                              ),
                                          runclass='')


##
## 
class caesar_cipher:

    def algorithm():
        try: 
            plaintext = str(caesar_cipher_objects['plaintext'].meta.text)
            key = int(caesar_cipher_objects['key'].meta.text)
        except:
            print('type error')
            return

        alphablet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        replaced = alphablet[key%26:] + alphablet[:key%26]
        
        caesar_cipher_objects['replaced'].meta.text = '"'+replaced+'"'
       
        ciphertext = ''

        # Convert to ciphertext
        for char in plaintext:
            if char.isalpha():
                cipherchar = replaced[alphablet.index(char.upper())]
                if not char.isupper(): cipherchar = cipherchar.lower()
                ciphertext += cipherchar

            else: ciphertext += char

        # Save it to data
        caesar_cipher_objects['ciphertext'].meta.text = ciphertext

        # Print data to screen
        textfield_event.update_textfield(screen, caesar_cipher_objects['replaced'], False)
        textfield_event.update_textfield(screen, caesar_cipher_objects['ciphertext'], False)

        return ciphertext
    
    def run():
        # Load the screen
        pygame_ess.load_screen(screen, caesar_cipher_objects)
        caesar_cipher.algorithm()
         
        while True:
            # Check for selection
            selection_result = pygame_ess.selection(screen, caesar_cipher_objects)
            selection_result_key, selection_result_value = list(selection_result.keys())[0], list(selection_result.values())[0]
            
            # Button pressed
            if selection_result_key == 'button':
                if selection_result_value == True: pygame_ess.load_screen(screen, caesar_cipher_objects)
                elif selection_result_value == 'back': return True
            
            # Testfield pressed
            elif selection_result_key == 'textfield':
                # Update ciphertext
                caesar_cipher.algorithm()

            if pygame_ess.buffer(): return True


##
## Main loop
if __name__ == "__main__":
    # Run home screen
    caesar_cipher.run()

    # Done! Time to quit.
    print('Exiting program...')
    pygame.quit()
