######################################
# Import and initialize the librarys #
######################################
import pygame
from pygame_ess import pygame_ess
import time


##################
# Initialization #
##################
pygame.init()

# Set up the drawing window
window_size = (1024, 768)
screen = pygame.display.set_mode((1024, 768))
window = pygame.surface.Surface((window_size))


#################################################
# Handles textfield objects and keyboard input #
#################################################
class textfield_event:
    '''Handles textfield objects and keyboard input'''

    def update_textfield(textfield_object, selected=True, backspace=False):
        '''Update the text displayed on screen'''

        # textfield is selected
        if selected: 
            screen.blit(textfield_object.images['textfield_selected'], (textfield_object.frame.image_coord()))
            if not backspace: textfield_object.meta.text += '_'
        
        # textfield not selected
        else: screen.blit(textfield_object.images['textfield'], (textfield_object.frame.image_coord()))

        # Render the text
        screen.blit(textfield_object.meta.render_text(), textfield_object.frame.box_coord())

        # Remove the '_'
        if selected and not backspace: textfield_object.meta.text = textfield_object.meta.text[:-1]

        # Output to screen
        pygame_ess.update()


    def run(textfield_object):
        '''keyboard input'''

        textfield_event.update_textfield(textfield_object, True)

        # Variables
        key_pressed = []
        time_pressed = 0
        repeat_interval = 0.7

        while True:
            for event in pygame.event.get():
                # if keyboard is pressed
                if event.type == pygame.KEYDOWN:

                    # Exit textfield if click return or escape
                    if event.key in [pygame.K_RETURN, pygame.K_ESCAPE]:
                        textfield_event.update_textfield(textfield_object, False)
                        return textfield_event

                    # Allow only unicode characters and backspace
                    elif 32 <= event.key <= 127 or event.key == pygame.K_BACKSPACE:
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
                    if not textfield_object.in_box(pygame.mouse.get_pos()):
                        textfield_event.update_textfield(textfield_object, False)
                        return textfield_event

                # Quit program
                elif event.type == pygame.QUIT: return 'quit'


            # Apply keypress, key repeat based on repeat interval in seconds
            if key_pressed != [] and time.time() - time_pressed >= repeat_interval:
                # remove character
                if key_pressed[-1].key == pygame.K_BACKSPACE:
                    textfield_object.meta.text = textfield_object.meta.text[:-1]
                    textfield_event.update_textfield(textfield_object, True, True)
                    textfield_event.update_textfield(textfield_object, True)

                # Add character
                else: 
                    textfield_object.meta.text += key_pressed[-1].unicode
                    textfield_event.update_textfield(textfield_object, True, True)
                    textfield_event.update_textfield(textfield_object, True)

                time_pressed = time.time()
                if repeat_interval > 0.03: repeat_interval /= 3