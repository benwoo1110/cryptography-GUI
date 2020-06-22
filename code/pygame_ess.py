######################################
# Import and initialize the librarys #
######################################
import logging
import pygame
import glob
import os
import traceback
import textwrap


##################
# Initialization #
##################
logging.info('Loading pygame essentials...')
pygame.init()
screen = pygame.display.set_mode((1024, 768))


########################
# Essentials functions #
########################
class pygame_ess:
    '''Essentials functions and variables for pygame'''


    #############################
    # Shared / common variables #
    #############################
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # Common defined colours
    class colour:
        '''Colour types in RGB form'''
        black = (0, 0, 0)
        white = (255, 255, 255)
        red = (255, 0, 0)
        gray = (43, 43, 43)
        whiteish = (213, 213, 213)
    

    ###############
    # Load events #
    ###############
    class load:
        def images(image_page:list, file_type:str = '.png', is_alpha:bool = False) -> bool:
            # Define variables
            images = dict()
            image_dir = 'images/{}/'.format('/'.join(image_page))

            # If in code directory and not root, go back a step
            if os.path.basename(os.getcwd()) == 'code': image_dir = '../' + image_dir
            
            # Get all image file from givent directory
            image_dir_list = glob.glob(image_dir+"*"+file_type)

            # Load them into pygame
            for image in image_dir_list:
                image_name = image.split('/')[-1].split('\\')[-1].split('.')[0]
                if is_alpha: images[image_name] = pygame.image.load(image).convert_alpha()
                else: images[image_name] = pygame.image.load(image).convert()

            return images

        def text(surface, object):
            # Grap text_data
            text_data = object.meta

            # Warp text if specified
            if text_data.warp_text != None:
                warpped_text = textwrap.wrap(text_data.text, width=text_data.warp_text)

                for line in range(len(warpped_text)):
                    if text_data.align == 'left': warpped_text[line] = '{1:<{0}}'.format(text_data.warp_text, warpped_text[line]).rstrip()
                    elif text_data.align == 'center': warpped_text[line] = '{1:^{0}}'.format(text_data.warp_text, warpped_text[line]).rstrip()
                    elif text_data.align == 'right': warpped_text[line] = '{1:>{0}}'.format(text_data.warp_text, warpped_text[line]).rstrip()
                    else: logging.error('Invalid alignment type {}'.format(text_data.align))

            # No text wrapping defined
            else: warpped_text = [text_data.text]

            # Generate surface for text
            text_surface = pygame.surface.Surface(object.frame.box_size())

            # Render multi line text
            h = 0
            for line in warpped_text:
                line_text = pygame.font.Font(text_data.font_type, text_data.font_size)
                rendered_text = line_text.render(line, True, text_data.colour)
                text_surface.blit(rendered_text, (0, h))
                h += line_text.size(line)[1]

            # Load to surface
            surface.blit(text_surface, (object.frame.box_coord()))

        def object(surface, object, state:str = '', load_text:bool = True) -> None:
            surface.blit(object.images[object.type+state], (object.frame.image_coord()))

            # Load text of object is a textfield
            if object.type == 'textfield': pygame_ess.load.text(surface, object)

        def objects(surface, objects:dict, names:list) -> None:
            # Loop through object specified and load them
            for name in names:
                # Try to load object specified
                try: pygame_ess.load.object(surface, objects[name])
                # Error loading object
                except: logging.error('[{}] {} object not in objects dictionary.'.format(window.name, name))

        def surface(surface, objects:dict):
            # Load objects to window
            for object in objects.values():
                # Load image of item
                pygame_ess.load.object(surface, object)


    ##################
    # Display events #
    ##################
    class display:
        def object(window, object, state:str = '', direct_to_screen:bool = False) -> None:
            if direct_to_screen: 
                screen.blit(object.images[object.type+state], (object.frame.image_coord()))
                pygame_ess.update()
            
            else: 
                pygame_ess.load.object(window.Window, object, state)
                pygame_ess.display.screen(window)

        def objects(window, objects:dict, names:list, direct_to_screen:bool = False) -> None:
            # Draw direct to screen
            if direct_to_screen:
                # Loop through object specified and load them
                for name in names:
                    # Try to load object specified
                    try: screen.blit(objects[name].images[objects[name].type], (objects[name].frame.image_coord()))
                    # Error loading object
                    except: logging.error('[{}] {} object not in objects dictionary.'.format(window.name, name))
                
                pygame_ess.update()

            # Load objects to surface, then display to screen
            else:
                pygame_ess.load.objects(window.Window, objects, names)
                pygame_ess.display.screen(window)

        def screen(window, update_all:bool = False, objects:dict = None) -> None:
            # Update all objects of the surface
            if update_all: pygame_ess.load.surface(window.Window, objects)

            # Ouput window to screen
            screen.blit(window.Window, (window.frame.bx, window.frame.by))

            # Draw to screen
            pygame_ess.update()


    #####################
    # Interaction event #
    #####################
    class event:
        def selection(window, selection_objects:dict, direct_to_screen:bool = False) -> dict:
            selection_result = {'object_name':'', 'object_type':'', 'action_result':''}

            for selection_object in selection_objects.values():
                # Skip selection check if runclass is empty
                if selection_object.runclass != None: 

                    # Check if mouse in selection object box
                    mouse_hover_over_object  = False
                    while selection_object.in_box(pygame.mouse.get_pos(), window.frame.box_coord()):
                        # Change to hover type
                        if selection_object.hover_action and not mouse_hover_over_object:
                            # Draws hover to surface
                            pygame_ess.display.object(window, selection_object, '_hover', direct_to_screen)
                            mouse_hover_over_object = True
                            logging.debug('[{}] Hovered on {} {}'.format(window.name, selection_object.name, selection_object.type))

                        # Run click event
                        click_result = pygame_ess.event.click(window, selection_object) 

                        # If clicked on object
                        if click_result != False: 
                            # Remove mouse hover
                            if mouse_hover_over_object: pygame_ess.load.object(window.Window, selection_object, '', direct_to_screen)
                            
                            # Load back previous screen
                            if click_result == True: 
                                pygame_ess.display.screen(window)
                                logging.info('loaded '+window.name)

                            # Stores click_result
                            selection_result['object_name'] = selection_object.name
                            selection_result['object_type'] = selection_object.type
                            selection_result['action_result'] = click_result

                            # Return data of click result
                            logging.info('[{}] object_name:{}, object_type:{}, action_result:{}'.format(window.name, selection_result['object_name'], selection_result['object_type'], selection_result['action_result']))
                            return selection_result

                    # Moved out of hitbox
                    if mouse_hover_over_object: pygame_ess.display.object(window, selection_object, '', direct_to_screen)  

            # No selections/clicks were made
            return selection_result

        def click(window, selection_object) -> any:
            for event in pygame.event.get():                
                # Check for left click
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    logging.info('[{}] Clicked on {} {}'.format(window.name, selection_object.name, selection_object.type))

                    # When there is no function to run
                    if type(selection_object.runclass) == str: return selection_object.runclass

                    # Load new screen
                    try: 
                        # Use selection_object as parameter
                        if selection_object.runclass_parameter == True: return selection_object.runclass(window, selection_object)
                        # No parameter needed
                        elif selection_object.runclass_parameter == False: return selection_object.runclass()
                        # Use custom parameter
                        else: return selection_object.runclass(selection_object.runclass_parameter)
                    
                    # When errors loading screen/runclass
                    except: 
                        logging.error('error running {} runclass.'.format(selection_object.runclass))
                        return True

                # When press closed windows
                if event.type == pygame.QUIT: return 'quit'

                pygame_ess.event.scroll(window, event)

            # User did not click
            return False  

        def scroll(window, event):
            # Check if scrolling is needed
            if 768 - window.frame.h < 0:
                # Check of scroll action
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Scroll up
                    if event.button == 4:
                        window.frame.by = min(window.frame.by + 35, 0)
                        pygame_ess.display.screen(window)

                    # Scroll down
                    elif event.button == 5:
                        window.frame.by = max(window.frame.by - 35, min(768 - window.frame.h, 0))
                        pygame_ess.display.screen(window)


    ########################
    # Other core functions #
    ########################
    def update(tick:int = 60):
        pygame.display.flip()
        pygame.display.update()
        pygame.time.Clock().tick(tick)

    def buffer(window) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return True
            pygame_ess.event.scroll(window, event)

    def quit():
        print('Exiting program...')
        pygame.quit()