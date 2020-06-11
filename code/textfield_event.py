######################################
# Import and initialize the librarys #
######################################
import pygame
from pygame_ess import pygame_ess


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

    def update_textfield(textfield_object, selected=True, back=False):
        '''Update the text displayed on screen'''

        # textfield is selected
        if selected: 
            screen.blit(textfield_object.images['textfield_selected'], (textfield_object.frame.image_coord()))
            if not back: textfield_object.meta.text += '_'
        
        # textfield not selected
        else: 
            screen.blit(textfield_object.images['textfield'], (textfield_object.frame.image_coord()))

        # Render the text
        screen.blit(textfield_object.meta.render_text(), textfield_object.frame.box_coord())

        # Remove the '_'
        if selected and not back: textfield_object.meta.text = textfield_object.meta.text[:-1]

        pygame_ess.update()


    def run(textfield_object):
        '''keyboard input'''

        textfield_event.update_textfield(textfield_object, True)

        while True:
            for event in pygame.event.get():
                # if keyboard is pressed
                if event.type == pygame.KEYDOWN:
                    # Exit textfield
                    if event.key in [pygame.K_RETURN, pygame.K_ESCAPE]:
                        textfield_event.update_textfield(textfield_object, False)
                        return textfield_object
                   
                    # remove character
                    elif event.key == pygame.K_BACKSPACE:
                        textfield_object.meta.text = textfield_object.meta.text[:-1]
                        textfield_event.update_textfield(textfield_object, True, True)
                        textfield_event.update_textfield(textfield_object, True)
                    
                    # Add character
                    elif event.unicode != '': 
                        textfield_object.meta.text += event.unicode
                        textfield_event.update_textfield(textfield_object, True, True)
                        textfield_event.update_textfield(textfield_object, True)

                # Exit textfield
                elif event.type == pygame.QUIT: 
                    textfield_event.update_textfield(textfield_object, False)
                    return textfield_object

                # Exit textfield if click out
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # Check clicked outside of textfield
                    if not textfield_object.in_box(pygame.mouse.get_pos()):
                        textfield_event.update_textfield(textfield_object, False)
                        return textfield_object