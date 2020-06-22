######################################
# Import and initialize the librarys #
######################################
import logging
from pygame_ess import pygame_ess
from item_storage import *

logging.debug('Initialising shared objects...')


#######################
# Load shared objects #
#######################
shared_objects:dict = dict()

shared_objects['back'] = item(name='back',
                              type='button',
                              images=pygame_ess.load.images(['shared_objects', 'back']),
                              frame=coord(
                                        47, 28,
                                        162, 67,
                                        0, 0
                                        ),
                              runclass='back')
            
shared_objects['info'] = item(name='info',
                            type='button',
                            images=pygame_ess.load.images(['shared_objects', 'info']),
                            frame=coord(
                                        813, 28,
                                        162, 67,
                                        814, 0
                                        ),
                            runclass='info')


######################################
# Load background and shared objects #
######################################
class common_objects:
    def load(objects:dict, page_name:str, shares:list = [], background:bool = True, is_alpha:bool = False) -> dict:
        # Load background
        if background:
            objects['background'] = item(name=page_name+' background', 
                                        type='background', 
                                        images=pygame_ess.load.images([page_name], is_alpha=is_alpha),
                                        frame=coord(
                                                0, 0,
                                                1024, 768,
                                                0, 0))

        # Load common shred objects needed
        for share in shares:
            try: objects[share] = shared_objects[share]
            except: print('Object {} not founded.'.format(share))

        return objects