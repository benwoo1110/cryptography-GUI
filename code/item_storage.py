######################################
# Import and initialize the librarys #
######################################
import pygame
import os
from input_validation import input_validation


#######################################
# Storage images and its cooridinates #
#######################################
class coord:
    def __init__(self, bx:int = 0, by:int = 0, w:int = 0, h:int = 0, ix:int = 0, iy:int = 0):
        self.bx = bx
        self.by = by
        self.w = w
        self.h = h
        self.ix = ix
        self.iy = iy

    def box_size(self):
        return (self.w, self.h)

    def box_coord(self):
        return (self.bx, self.by)
    
    def image_coord(self):
        return (self.ix, self.iy)

    def __str__(self):
        return '''
    bx:{} by:{} 
    w:{} h:{}
    ix:{} iy:{} 
        '''.format(self.bx, self.by, self.w, self.h, self.ix, self.iy)


#####################################
# Stores data for text & textfields #
#####################################
class text_data:
    def __init__(self, text:str = '', font_type:str = '', is_custom_font:bool = True, font_size:int = 36, colour:set = (0, 0, 0), validation:input_validation = input_validation.text()):
        self.text = text
        self.font_size = font_size
        self.colour = colour
        self.validation = validation

        # Check if custom font is defined
        if font_type == '':
            self.font_type = None
            self.is_custom_font = False

        # Get font file if its custom
        elif is_custom_font:
            # Get font type file
            font_dir = 'font/'+font_type

            # If in code directory and not root, go back a step
            if os.path.basename(os.getcwd()) == 'code': font_dir = '../' + font_dir
            
            # Save dir of custom font
            self.font_type = font_dir
            self.is_custom_font = True

    def render_text(self):
        font = pygame.font.Font(self.font_type, self.font_size)
        return font.render(self.text, True, self.colour)

    def __str__(self):
        return '''
    text: {}
    font_type: {}
    is_custom_font: {}
    font_size: {}
    colour: {}
    validation: {}
        '''.format(self.text, self.font_type, self.is_custom_font, self.font_size, self.colour, self.validation)


###########################
# Storages UI object data #
###########################
class item:
    def __init__(self, name:str = 'name', type:str = 'button', meta:dict = {}, images:dict = {}, frame:coord = coord(), hover_action:bool = None, runclass = None, runclass_parameter:bool = None):
        # Stores object data
        self.name = name
        self.type = type
        self.meta = meta
        self.images = images
        self.frame = frame
        self.hover_action = hover_action
        self.runclass = runclass
        self.runclass_parameter = runclass_parameter

        # Set to default hover_action if not defined
        if hover_action == None:
            if self.type == 'button': self.hover_action = True
            else: hover_action = False

        # Set to default runclass_parameter if not defined
        if runclass_parameter == None:
            if self.type == 'textfield': self.runclass_parameter = True
            else: self.runclass_parameter = False

    def in_box(self, mouse_pos):
        return self.frame.bx < mouse_pos[0] < self.frame.bx + self.frame.w and self.frame.by < mouse_pos[1] < self.frame.by + self.frame.h 

    def __str__(self):
        return '''
name: {}
type: {}
meta:{} 
images: {} 
frame: {}
hover_action: {}
runclass: {}
runclass_parameter: {}
        '''.format(self.name, self.type, self.meta, list(self.images.keys()), self.frame, self.hover_action, self.runclass, self.runclass_parameter)
