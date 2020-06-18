######################################
# Import and initialize the librarys #
######################################
import pygame
import logging
import glob
from item_storage import *
import os
import traceback


##################
# Initialization #
##################
logging.info('Loading pygame essentials...')
screen = pygame.display.set_mode((1024, 768))


########################
# Essentials functions #
########################
class pygame_ess:
    '''Essentials functions and variables for pygame'''


    #############################
    # Shared / common variables #
    #############################
    alphabet = 'ABCDDEFHIJKLMNOPQRSTUVWXYZ'

    # Common defined colours
    class colour:
        '''Colour types in RGB form'''
        black = (0, 0, 0)
        white = (255, 255, 255)
        red = (255, 0, 0)
        gray = (43, 43, 43)
    

    ###############
    # Load events #
    ###############
    def load_images(image_page:list, file_type:str = '.png', is_alpha:bool = False) -> bool:
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

    def load_essential_objects(objects:dict, page_name:str, shares:list = [], background:bool = True, is_alpha:bool = False) -> dict:
        # Load background
        if background:
            objects['background'] = item(name=page_name+' background', 
                                        type='background', 
                                        images=pygame_ess.load_images([page_name], is_alpha=is_alpha),
                                        frame=coord(
                                                0, 0,
                                                1024, 768,
                                                0, 0
                                                )
                                        )

        # Load common shred objects needed
        for share in shares:
            try: objects[share] = shared_objects[share]
            except: print('Object {} not founded.'.format(share))

        return objects

    def load_screen(window:surface):
        # Ouput window to screen
        screen.blit(window.Window, (window.frame.bx, window.frame.by))

        # Draw to screen
        pygame_ess.update()


    #####################
    # Interaction event #
    #####################
    def selection_event(window, selection_objects:dict) -> dict:
        selection_result = {'object_name':'', 'object_type':'', 'action_result':''}
        Window = window.Window

        for selection_object in selection_objects.values():
        
            # Skip selection check if runclass is empty
            if selection_object.runclass != None: 

                # Check if mouse in selection object box
                mouse_hover_over_object  = False
                while selection_object.in_box(pygame.mouse.get_pos(), window.frame.by):
                    # Change to hover type
                    if selection_object.hover_action and not mouse_hover_over_object:
                        Window.blit(selection_object.images[selection_object.type+'_hover'], (selection_object.frame.image_coord()))
                        mouse_hover_over_object = True
                        pygame_ess.load_screen(window)
                        logging.debug('Hovered on '+selection_object.name+' button.')

                    # Run click event
                    click_result = pygame_ess.click_event(window, selection_object) 

                    # If clicked on object
                    if click_result != False: 
                        # Remove mouse hover
                        if mouse_hover_over_object:
                            Window.blit(selection_object.images[selection_object.type], (selection_object.frame.image_coord()))
                        
                        # Load back previous screen
                        if click_result == True: 
                            pygame_ess.load_screen(window)

                        # Stores click_result
                        selection_result['object_name'] = selection_object.name
                        selection_result['object_type'] = selection_object.type
                        selection_result['action_result'] = click_result

                        # Return data of click result
                        logging.info('[{}] object_name:{}, object_type:{}, action_result:{}'.format(window.name, selection_result['object_type'], selection_result['object_name'], selection_result['action_result']))
                        return selection_result

                # Moved out of hitbox
                if mouse_hover_over_object:
                    Window.blit(selection_object.images[selection_object.type], (selection_object.frame.image_coord()))
                    pygame_ess.load_screen(window)

        # No selections/clicks were made
        return selection_result

    def click_event(window, selection_object) -> any:
        for event in pygame.event.get():                
            # Check for left click
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                logging.info('clicked on '+selection_object.name+' '+selection_object.type)

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
                    print('error running', selection_object.name)
                    traceback.print_exc()
                    return True

            pygame_ess.scroll_event(window, event)

        # User did not click
        return False  

    def scroll_event(window, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Scroll up
            if event.button == 4:
                window.frame.by = min(window.frame.by + 35, 0)
                pygame_ess.load_screen(window)

            # Scroll down
            elif event.button == 5:
                window.frame.by = max(window.frame.by - 35, min(768 - window.frame.h, 0))
                pygame_ess.load_screen(window)


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
            pygame_ess.scroll_event(window, event)

    def quit():
        print('Exiting program...')
        pygame.quit()


#######################
# Load shared objects #
#######################
logging.debug('Initialising shared objects...')
shared_objects:dict = dict()

shared_objects['back'] = item(name='back',
                              type='button',
                              images=pygame_ess.load_images(['shared_objects', 'back']),
                              frame=coord(
                                        47, 28,
                                        162, 67,
                                        0, 0
                                        ),
                              runclass='back')
            
shared_objects['info'] = item(name='info',
                            type='button',
                            images=pygame_ess.load_images(['shared_objects', 'info']),
                            frame=coord(
                                        813, 28,
                                        162, 67,
                                        814, 0
                                        ),
                            runclass='info')