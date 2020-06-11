##
## Import and initialize the librarys
import pygame
from pygame_ess import pygame_ess


class textfield_event:

    def update_textfield(screen, textfield_object, selected=True, back=False):
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


    def run(screen, textfield_object):
        textfield_event.update_textfield(screen, textfield_object, True)

        while True:
            for event in pygame.event.get():
                # if keyboard is pressed
                if event.type == pygame.KEYDOWN:
                    # Exit textfield
                    if event.key in [pygame.K_RETURN, pygame.K_ESCAPE]:
                        textfield_event.update_textfield(screen, textfield_object, False)
                        return textfield_object
                   
                    # remove character
                    elif event.key == pygame.K_BACKSPACE:
                        textfield_object.meta.text = textfield_object.meta.text[:-1]
                        textfield_event.update_textfield(screen, textfield_object, True, True)
                        textfield_event.update_textfield(screen, textfield_object, True)
                    
                    # Add character
                    elif event.unicode != '': 
                        textfield_object.meta.text += event.unicode
                        textfield_event.update_textfield(screen, textfield_object, True, True)
                        textfield_event.update_textfield(screen, textfield_object, True)

                # Exit textfield
                elif event.type == pygame.QUIT: 
                    textfield_event.update_textfield(screen, textfield_object, False)
                    return textfield_object

                # Exit textfield if click out
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if not textfield_object.in_box(pygame.mouse.get_pos()):
                        # Check if not in box
                        print(textfield_object.meta.text)
                        textfield_event.update_textfield(screen, textfield_object, False)
                        return textfield_object