######################################
# Import and initialize the librarys #
######################################
import logging
import pygame
from item_storage import *
from pygame_ess import pygame_ess
from textfield_event import textfield_event


##################
# Initialization #
##################
logging.info('Loading invalid input...')
screen = pygame.display.set_mode((1024, 768))


#########################
# Variables declaration #
#########################
logging.debug('Initialising invalid input variables...')
page_name:str = 'invalid_input'
invalid_input_objects:dict = dict()


##############################
# Load invalid input objects #
##############################
logging.debug('Initialising invalid input objects...')

# Load essentials images
pygame_ess.load_essential_objects(invalid_input_objects, page_name, is_alpha=True)

# Alert
invalid_input_objects['alert'] = item(name='alert',
                                          type='alert',
                                          images=pygame_ess.load_images([page_name, 'alert'], is_alpha=True),
                                          frame=coord(
                                              306, 291, 
                                              412, 186, 
                                              0, 0),)

# Invalid input message
invalid_input_objects['message'] = item(name='message',
                                        type='textfield',
                                        meta=text_data(
                                                text='Oh no! Your input is invalid!',
                                                font_type='Monaco.dfont',
                                                font_size=22,
                                                warp_text=28,
                                                align='center',
                                                colour=pygame_ess.colour.whiteish
                                                ),
                                        images=pygame_ess.load_images([page_name, 'message']),
                                        frame=coord(
                                              333, 359, 
                                              360, 60, 
                                              333, 359),)

# ok button
invalid_input_objects['ok'] = item(name='ok!',
                                          type='button',
                                          images=pygame_ess.load_images([page_name, 'ok']),
                                          frame=coord(
                                              422, 429, 
                                              179, 35, 
                                              422, 429
                                              ),
                                          runclass='back')


###################
# Generate window #
###################
logging.info('Initialising invalid input window...')
invalid_input_window:surface = surface(invalid_input_objects, name=page_name, is_alpha = True)


#######################
# Invalid Input Alert #
#######################
class invalid_input:
    '''cryptography home page'''

    def run(invalid_message:str = 'Oh no! Your input is invalid!'):
        '''Display cryptography home page'''

        # Set message
        invalid_input_objects['message'].meta.text = invalid_message
        # Load the screen
        textfield_event.update_textfield(invalid_input_window, invalid_input_objects['message'], False)
        logging.info('Loaded invalid input window.')

        while True:
            # Check for selection
            selection_result:dict = pygame_ess.selection_event(invalid_input_window, invalid_input_objects, direct_to_screen=True)

            # Quit program
            if selection_result['action_result'] == 'quit' or pygame_ess.buffer(invalid_input_window): 
                return 'quit'

            # Dismiss alert
            if selection_result['action_result'] == 'back': return True


#############
# Main loop #
#############
if __name__ == "__main__":
    pygame.init()
    # Run home screen
    invalid_input.run()

    # Done! Time to quit.
    pygame_ess.quit()