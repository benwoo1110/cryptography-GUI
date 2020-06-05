##
## Storage images and its cooridinates
class coord:
    def __init__(self, bx=0, by=0, w=0, h=0, ix=0, iy=0):
        self.bx = bx
        self.by = by
        self.w = w
        self.h = h
        self.ix = ix
        self.iy = iy

    def button_coord(self):
        return (self.bx, self.by)
    
    def image_coord(self):
        return (self.ix, self.iy)

    def __str__(self):
        return 'x:{} y:{} w:{} h:{}'.format(self.bx, self.by, self.w, self.h)


class image_item:
    def __init__(self, name='image_item', images=dict(), button=coord(), hover=False):
        self.name = name
        self.images = images
        self.button = button
        self.hover = hover

    def __str__(self):
        return 'name={} images={} button={}'.format(self.name, self.images, self.button)

    def in_box(self, mouse_pos):
        return self.button.bx < mouse_pos[0] < self.button.bx + self.button.w and self.button.by < mouse_pos[1] < self.button.by + self.button.h 
