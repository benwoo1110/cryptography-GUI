######################################
# Import and initialize the librarys #
######################################
import logging
import pygame
from pygame_ess import pygame_ess
import time


##################
# Initialization #
##################
screen = pygame.display.set_mode((1024, 768))


#################################################
# Handles textfield objects and keyboard input #
#################################################
class textfield_event:
    '''Handles textfield objects and keyboard input'''

    def update_textfield(window, textfield_object, selected=True, backspace=False):
        '''Update the text displayed on screen'''
        
        Window = window.Window

        # textfield is selected
        if selected: 
            Window.blit(textfield_object.images['textfield_selected'], (textfield_object.frame.image_coord()))
            if not backspace: textfield_object.meta.text += '_'
        
        # textfield not selected
        else: Window.blit(textfield_object.images['textfield'], (textfield_object.frame.image_coord()))

        # Render the text
        Window.blit(textfield_object.meta.render_text(), textfield_object.frame.box_coord())

        # Remove the '_'
        if selected and not backspace: textfield_object.meta.text = textfield_object.meta.text[:-1]

        # Output to screen
        pygame_ess.display.screen(window)


    def run(window, textfield_object) -> str:
        '''keyboard input'''

        # Check if there is input validation
        if textfield_object.meta.validation == None: logging.warn('No input validation specified.')

        textfield_event.update_textfield(window, textfield_object, True)
        logging.info('Loaded '+textfield_object.name+' textfield.')

        # Key repeat variables
        key_pressed = []
        time_pressed = 0
        repeat_interval = 0.75

        while True:
            for event in pygame.event.get():
                # if keyboard is pressed
                if event.type == pygame.KEYDOWN:

                    # Exit textfield if click return or escape
                    if event.key in [pygame.K_RETURN, pygame.K_ESCAPE]:

                        # Check if input is valid
                        if textfield_object.meta.validation == None or textfield_object.meta.validation.check(textfield_object.meta.text):
                            # Exit from texfield if so
                            textfield_event.update_textfield(window, textfield_object, False)
                            logging.info('Exited '+textfield_object.name+' textfield.')
                            return textfield_object.meta.text
                        
                        # Load back textfield screen
                        else: textfield_event.update_textfield(window, textfield_object, True)

                    # Allow only based on validation defined
                    elif event.key in textfield_object.meta.validation.chars_allowed:
                        key_pressed.append(event)

                # Key is released
                elif event.type == pygame.KEYUP:
                    # reset key variables
                    # Variables
                    for pressed in range(len(key_pressed)):
                        if key_pressed[pressed].key == event.key:
                            key_pressed.pop(pressed)
                            time_pressed = 0
                            repeat_interval = 1.2
                            break

                # Exit textfield if click out
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # Check clicked outside of textfield
                    if not textfield_object.in_box(pygame.mouse.get_pos(), window.frame.box_coord()):

                        # Check if input is valid
                        if textfield_object.meta.validation == None or textfield_object.meta.validation.check(textfield_object.meta.text):
                            # Exit from texfield if so
                            textfield_event.update_textfield(window, textfield_object, False)
                            logging.info('Exited '+textfield_object.name+' textfield.')
                            return textfield_object.meta.text

                        # Load back textfield screen
                        else: textfield_event.update_textfield(window, textfield_object, True)


                # Quit program
                elif event.type == pygame.QUIT: return 'quit'

                # check for Scroll
                pygame_ess.event.scroll(window, event)

            # Apply keypress, key repeat based on repeat interval in seconds
            if key_pressed != [] and time.time() - time_pressed >= repeat_interval:

                new_text = textfield_object.meta.text

                # remove character
                if key_pressed[-1].key == pygame.K_BACKSPACE: new_text = textfield_object.meta.text[:-1]
                    
                # Add character
                else: new_text += key_pressed[-1].unicode

                # Do not exceed max length
                if len(new_text) <= textfield_object.meta.validation.max_length:
                    # Stores the new_text
                    textfield_object.meta.text = new_text
                    # Update textfield
                    textfield_event.update_textfield(window, textfield_object, True, True)
                    textfield_event.update_textfield(window, textfield_object, True)

                # Setup for next key repeat
                time_pressed = time.time()
                if repeat_interval > 0.025: repeat_interval /= 4
