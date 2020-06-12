######################################
# Import and initialize the librarys #
######################################
import pygame
import glob
from item_storage import *
import os
import traceback


##################
# Initialization #
##################
pygame.init()

# Set up the drawing window
window_size = (1024, 768)
screen = pygame.display.set_mode((1024, 768))
window = pygame.surface.Surface((window_size))


########################
# Essentials functions #
########################
class pygame_ess:
    '''Essentials functions and variables for pygame'''

    # Shared / common variables
    alphabet = 'ABCDDEFHIJKLMNOPQRSTUVWXYZ'

    class colour:
        '''Colour types in RGB form'''
        black = (0, 0, 0)
        white = (255, 255, 255)
        red = (255, 0, 0)
    
    def load_images(image_page:list, file_type:str = '.png'):
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
            images[image_name] = pygame.image.load(image).convert()

        return images

    def load_essential_objects(objects:dict(), page_name:str, shares:list = [], background:bool = True):
        if background:
            objects['background'] = item(name='cryptography background', 
                                                type='background', 
                                                images=pygame_ess.load_images([page_name]))

        for share in shares:
            try: objects[share] = shared_objects[share]
            except: print('Object {} not founded.'.format(share))

        return objects

    def load_screen(screen_objects):
        # Load all items
        for screen_object in screen_objects.values():
            # Load image of item
            screen.blit(screen_object.images[screen_object.type], screen_object.frame.image_coord())

            # Load text for textfield objects
            if screen_object.type == 'textfield':
                screen.blit(screen_object.meta.render_text(), screen_object.frame.box_coord())

        # Output to screen
        pygame_ess.update()

    def selection_event(selection_objects) -> dict:
        selection_result = {'object_type':'', 'object_name':'', 'action_result':''}

        for selection_object in selection_objects.values():
        
            # Skip selection check if runclass is empty
            if not ( type(selection_object.runclass) == str and selection_object.runclass.strip() == '' ): 

                # Check if mouse in selection object box
                mouse_hover_over_object  = False
                while selection_object.in_box(pygame.mouse.get_pos()):

                    # Change to hover type
                    if selection_object.hover_action and not mouse_hover_over_object:
                        screen.blit(selection_object.images[selection_object.type+'_hover'], (selection_object.frame.image_coord()))
                        mouse_hover_over_object = True
                        pygame_ess.update()

                    # Run click event
                    click_result = pygame_ess.click_event(selection_object) 

                    # If clicked on object
                    if click_result != False: 
                        # Stores click_result
                        selection_result['object_type'] = selection_object.type
                        selection_result['object_name'] = selection_object.name
                        selection_result['action_result'] = click_result
                        # Return data of click result
                        print(selection_result)
                        return selection_result

                # Moved out of hitbox
                if mouse_hover_over_object:
                    screen.blit(selection_object.images[selection_object.type], (selection_object.frame.image_coord()))
                    selection_object.hover = False
                    pygame_ess.update()

        # No selections/clicks were made
        return selection_result

    def click_event(selection_object):
        for event in pygame.event.get():                
            # Check for left click
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                print("clicked", selection_object.type, selection_object.name)

                # When there is no function to run
                if type(selection_object.runclass) == str: return selection_object.runclass

                # Load new screen
                try: 
                    # Use selection_object as parameter
                    if selection_object.runclass_parameter == True: return selection_object.runclass(selection_object)
                    # No parameter needed
                    elif selection_object.runclass_parameter == False: return selection_object.runclass()
                    # Use custom parameter
                    else: return selection_object.runclass(selection_object.runclass_parameter)
                
                # When errors loading screen/runclass
                except: 
                    print('error running', selection_object.name)
                    traceback.print_exc()
                    return True

        # User did not click
        return False   

    def update(tick:int = 240):
        pygame.display.flip()
        pygame.display.update()
        pygame.time.Clock().tick(tick)

    def buffer() -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return True

    def quit():
        print('Exiting program...')
        pygame.quit()


#######################
# Load shared objects #
#######################
shared_objects = dict()

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