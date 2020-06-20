######################################
# Import and initialize the librarys #
######################################
import logging
import pygame
import os


#######################################
# Storage images and its cooridinates #
#######################################
class coord:
    def __init__(self, bx:int = 0, by:int = 0, w:int = 0, h:int = 0, ix:int = 0, iy:int = 0):
        self.bx:int = bx
        self.by:int = by
        self.w:int = w
        self.h:int = h
        self.ix:int = ix
        self.iy:int = iy

    def box_size(self) -> tuple: 
        return (self.w, self.h)

    def box_coord(self, surface_coord:tuple = (0, 0)) -> tuple: 
        return (self.bx + surface_coord[0], self.by + surface_coord[1])
    
    def image_coord(self, surface_coord:tuple = (0, 0)) -> tuple: 
        return (self.ix + surface_coord[0], self.iy + surface_coord[1])

    def __str__(self):
        return 'bx:{} by:{} w:{} h:{} ix:{} iy:{}'.format(self.bx, self.by, self.w, self.h, self.ix, self.iy)


#####################################
# Stores data for text & textfields #
#####################################
class text_data:
    def __init__(self, text:str = '', font_type:str = '', is_custom_font:bool = True, 
    font_size:int = 36, colour:set = (0, 0, 0), validation = None):
        self.text:str = text
        self.font_size:int = font_size
        self.colour:tuple = colour
        self.validation = validation

        # Check if custom font is defined
        if font_type == '':
            self.font_type = None
            self.is_custom_font = False

        # Get font file if its custom
        elif is_custom_font:
            # Get font type file
            font_dir:str = 'font/'+font_type

            # If in code directory and not root, go back a step
            if os.path.basename(os.getcwd()) == 'code': font_dir = '../' + font_dir
            
            # Save dir of custom font
            self.font_type = font_dir
            self.is_custom_font = True

    def render_text(self):
        font = pygame.font.Font(self.font_type, self.font_size)
        return font.render(self.text, True, self.colour)

    def __str__(self):
        return '''text:{}
      font_type:{}, is_custom_font:{}, font_size:{}, colour:{}
      validation:{}'''.format(self.text, self.font_type, self.is_custom_font, self.font_size, self.colour, self.validation)


###########################
# Storages UI object data #
###########################
class item:
    def __init__(self, name:str = 'name', type:str = 'object', meta:any = None, images:dict = {}, 
    frame:coord = coord(), hover_action:bool = None, runclass:any = None, runclass_parameter:bool = None):
        # Stores object data
        self.name:str = name
        self.type:str = type
        self.meta:any = meta
        self.images:dict = images
        self.frame:coord = frame
        self.hover_action:bool = hover_action
        self.runclass:any = runclass
        self.runclass_parameter:bool = runclass_parameter

        # Set to default hover_action if not defined
        if hover_action == None:
            if self.type == 'button': self.hover_action = True
            else: hover_action = False

        # Set to default runclass_parameter if not defined
        if runclass_parameter == None:
            if self.type == 'textfield': self.runclass_parameter = True
            else: self.runclass_parameter = False

        # Debug objects
        logging.debug(self.__str__())

    def in_box(self, mouse_pos:tuple, surface_coord:tuple = (0, 0)) -> bool:
        # Save surface coord to seperate variables
        scroll_x:int = surface_coord[0]
        scroll_y:int = surface_coord[1]
        # Return if in box
        return self.frame.bx + scroll_x < mouse_pos[0] < self.frame.bx + self.frame.w + scroll_x and self.frame.by + scroll_y < mouse_pos[1] < self.frame.by + self.frame.h + scroll_y

    def __str__(self):
        return '''
name:{}, type:{}, hover_action:{}
meta: {} 
images: {}
frame: {}
runclass:{}, runclass_parameter:{}'''.format(self.name, self.type, self.hover_action, self.meta, self.images, self.frame, self.runclass, self.runclass_parameter)


##########################
# Store suface of window #
##########################
class surface:
    def __init__(self, window_objects:dict, name:str = 'window', frame:coord = coord(bx=0, by=0, w=1024, h=None), background_fill:tuple = None, is_alpha:bool = False):
        # get the height of window if not defined
        if frame.h == None:
            frame.h = 0
            for window_object in window_objects.values():
                frame.h =  max(frame.h, window_object.frame.iy+window_object.frame.h)

        # Create window
        if is_alpha: window = pygame.surface.Surface((frame.w, frame.h), pygame.SRCALPHA)
        else:  window = pygame.surface.Surface((frame.w, frame.h))

        # Fill surface with default colour
        if background_fill == None:
            # Fill if surface doesnt need tranparency
            if not is_alpha: window.fill((43, 43, 43))
        # Fill with colour with user defined
        else: window.fill(background_fill)

        # Load objects to window
        for window_object in window_objects.values():
            # Load image of item
            window.blit(window_object.images[window_object.type], window_object.frame.image_coord())

            # Load text for textfield objects
            if window_object.type == 'textfield':
                window.blit(window_object.meta.render_text(), window_object.frame.box_coord())

        # Save to class
        self.name = name
        self.Window:pygame.surface.Surface = window.convert_alpha()
        self.frame:coord = frame
        self.background_fill:tuple = background_fill
        self.is_alpha:bool = is_alpha

        # Debug surface
        logging.debug(self.__str__())

    def __str__(self):
        return '''
name: {}
Window: {}
frame: {}
background_fill:{}, is_alpha{}'''.format(self.name, self.Window, self.frame, self.background_fill, self.is_alpha)