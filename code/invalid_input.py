######################################
# Import and initialize the librarys #
######################################
import pygame
from item_storage import *
from pygame_ess import pygame_ess


##################
# Initialization #
##################
pygame.init()
screen = pygame.display.set_mode((1024, 768))


#########################
# Variables declaration #
#########################
page_name:str = 'invalid_input'
invalid_input_objects:dict = dict()


##############################
# Load affine cipher objects #
##############################

# Load essentials images
pygame_ess.load_essential_objects(invalid_input_objects, page_name, is_alpha=True)

# Alert
invalid_input_objects['alert'] = item(name='alert',
                                          type='alert',
                                          images=pygame_ess.load_images([page_name, 'alert'], is_alpha=True),
                                          frame=coord(
                                              306, 291, 
                                              412, 186, 
                                              0, 0
                                              ),)

invalid_input_objects['ok'] = item(name='ok!',
                                          type='button',
                                          images=pygame_ess.load_images([page_name, 'ok'], ),
                                          frame=coord(
                                              422, 429, 
                                              179, 35, 
                                              422, 429
                                              ),
                                          runclass='back')


###################
# Generate window #
###################
invalid_input_window:surface = surface(invalid_input_objects, is_alpha = True)


#######################
# Invalid Input Alert #
#######################
class invalid_input:
    '''cryptography home page'''

    def run():
        '''Display cryptography home page'''

        # Load the screen
        pygame_ess.load_screen(invalid_input_window)

        while True:
            # Check for selection
            selection_result:dict = pygame_ess.selection_event(invalid_input_window, invalid_input_objects)

            # Quit program
            if selection_result['action_result'] == 'quit' or pygame_ess.buffer(invalid_input_objects): 
                return 'quit'

            # Dismiss alert
            if selection_result['action_result'] == 'back': return True


#############
# Main loop #
#############
if __name__ == "__main__":
    # Run home screen
    invalid_input.run()

    # Done! Time to quit.
    pygame_ess.quit()