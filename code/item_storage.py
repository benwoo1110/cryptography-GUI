######################################
# Import and initialize the librarys #
######################################
import pygame


#######################################
# Storage images and its cooridinates #
#######################################
class coord:
    def __init__(self, bx=0, by=0, w=0, h=0, ix=0, iy=0):
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
        return 'x:{} y:{} w:{} h:{}'.format(self.bx, self.by, self.w, self.h)


#####################################
# Stores data for text & textfields #
#####################################
class text_data:
    def __init__(self, text='', font_type=None, font_size=36, colour=(255, 255, 255)):
        self.text = text
        self.font_type = '../font/'+font_type
        self.font_size = font_size
        self.colour = colour

    def render_text(self):
        font = pygame.font.Font(self.font_type, self.font_size)
        return font.render(self.text, True, self.colour)


###########################
# Storages UI object data #
###########################
class item:
    def __init__(self, name:str = 'name', type:str = 'button', meta:dict = {}, images:dict = {}, frame:coord = coord(), hover_action:bool = None, runclass:bool = None, runclass_parameter = None):
        # Stores object data
        self.name = name
        self.type = type
        self.meta = meta
        self.images = images
        self.frame = frame
        self.hover_action = hover_action
        self.runclass = runclass
        self.runclass_parameter= runclass_parameter

        # Set to default hover_action if not defined
        if hover_action == None:
            if self.type == 'button': self.hover_action = True
            else: hover_action = False

        # Set to default runclass_parameter if not defined
        if runclass_parameter == None:
            if self.type == 'textfield': self.runclass_parameter = True
            else: self.runclass_parameter = False

    def __str__(self):
        return 'meta={} images={} frame={}'.format(self.meta, self.images, self.frame)

    def in_box(self, mouse_pos):
        return self.frame.bx < mouse_pos[0] < self.frame.bx + self.frame.w and self.frame.by < mouse_pos[1] < self.frame.by + self.frame.h 
