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
button_types = {'back':'back', 'info':''}
caesar_cipher_objects = dict()


##
## Load home screen objects

# background image
caesar_cipher_objects['background'] = item(name='cryptography background',
                                           type='background', 
                                           images=pygame_ess.load_images([page_name]))

# Buttons
for button_type in button_types.keys():
    caesar_cipher_objects[button_type] = item(name=button_type,
                                              type='button',
                                              images=pygame_ess.load_images([page_name, button_type]),
                                              frame=coord(
                                                  47 + 766 * list(button_types.keys()).index(button_type), 28, 
                                                  162, 67, 
                                                  (48 + 766) * list(button_types.keys()).index(button_type), 0
                                                  ),
                                              runclass=button_types[button_type])

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

caesar_cipher_objects['alphablet'] = item(name='alphablet',
                                          type='text',
                                          meta=text_data(
                                              text='"ABCDEFGHIJKLMNOPQRSTUVWXYZ"',
                                              font_type='Monaco.dfont',
                                              font_size=34,
                                              colour=(255,255,255)
                                              ),
                                          images=pygame_ess.load_images([page_name, 'alphablet']),
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

caesar_cipher_objects['cyphertext'] = item(name='cyphertext',
                                          type='text',
                                          meta=text_data(
                                              text='cyphertext',
                                              font_type='Monaco.dfont',
                                              font_size=34,
                                              colour=(0,0,0)
                                              ),
                                          images=pygame_ess.load_images([page_name, 'cyphertext']),
                                          frame=coord(
                                              325, 574, 
                                              632, 62, 
                                              307, 564
                                              ),
                                          runclass='')


##
## 
class caesar_cipher:

    def algorithm(caesar_cipher_objects):
        
        try: 
            plaintext = str(caesar_cipher_objects['plaintext'].meta.text)
            key = int(caesar_cipher_objects['key'].meta.text)
        except:
            print('type error')
            return

        alphablet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        replaced = alphablet[key%26:] + alphablet[:key%26]
        
        caesar_cipher_objects['replaced'].meta.text = '"'+replaced+'"'
       
        cyphertext = ''

        # Convert to cyphertext
        for char in plaintext:
            if char.isalpha():
                cypherchar = replaced[alphablet.index(char.upper())]
                if not char.isupper(): cypherchar = cypherchar.lower()
                cyphertext += cypherchar

            else: cyphertext += char

        # Save it to data
        caesar_cipher_objects['cyphertext'].meta.text = cyphertext

        # Print data to screen
        textfield_event.update_textfield(screen, caesar_cipher_objects['replaced'], False)
        textfield_event.update_textfield(screen, caesar_cipher_objects['cyphertext'], False)

        return cyphertext
    
    def run():
        # Load the screen
        pygame_ess.load_screen(screen, caesar_cipher_objects)
        caesar_cipher.algorithm(caesar_cipher_objects)
         
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
                # Store back
                #caesar_cipher_objects[selection_result_value.name] = selection_result_value
                #pygame_ess.load_screen(screen, caesar_cipher_objects)

                # Update cyphertext
                caesar_cipher.algorithm(caesar_cipher_objects)

            if pygame_ess.buffer(): return True


##
## Main loop
if __name__ == "__main__":
    ##
    ## Run home screen
    caesar_cipher.run()
    
    # Done! Time to quit.
    pygame.quit()
