##
## Import and initialize the librarys
import pygame
from pygame_ess import pygame_ess


##
## Initialization
pygame.init()
pygame.font.init()

# Set up the drawing window
window_size = (1024, 768)
screen = pygame.display.set_mode((1024, 768))
window = pygame.surface.Surface((window_size))
pygame.display.set_caption("Cryptography")


##
## cipher classes to store images data and position
class coord:
    def __init__(self, x=0, y=0, w=0, h=0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def __str__(self):
        return 'x:{} y:{} w:{} h:{}'.format(self.x, self.y, self.w, self.h)

class cipher:
    def __init__(self, name='cipher', images=dict(), button=coord(), hover=False):
        self.name = name
        self.images = images
        self.button = button
        self.hover = hover

    def __str__(self):
        return 'name={} images={} button={}'.format(self.name, self.images, self.button)

    def in_box(self, mouse_pos):
        return self.button.x < mouse_pos[0] < self.button.x + self.button.w and self.button.y < mouse_pos[1] < self.button.y + self.button.h 


##
## Variables
image_dir = 'images/cryptography/'

cipher_types = ['caesar_cipher', 'monoalphabetic_cipher', 'homophonic_substitution_cipher',
                'polygram_subsitution_cipher', 'polyalphabetic_substitution_cipher']

home_screen = dict()


##
## Load home screen images

# background image
home_screen['background'] = pygame_ess.load_images(image_dir)

# cipher list
for cipher_type in cipher_types:
    home_screen[cipher_type] = cipher(cipher_type,
                                      pygame_ess.load_images(image_dir+cipher_type+'/'),
                                      coord(47, 112 + cipher_types.index(cipher_type) * 106, 929, 86))


##
## Key home screen functions
def load_home_screen():
    # Load background
    screen.blit(home_screen['background']['cryptography_bg'], (0,0))

    # Load each option
    for cipher_type in cipher_types:
        screen.blit(home_screen[cipher_type].images['button'], (0,home_screen[cipher_type].button.y))
        
    pygame_ess.update()

def click(cipher_type):
    clicked = False
    for event in pygame.event.get():
        # Check for left click
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            clicked = True
            print(cipher_type, 'is clicked.')

        

def selection():
    mouse_pos = pygame.mouse.get_pos()

    for cipher_type in cipher_types:
        while home_screen[cipher_type].in_box(mouse_pos):
            # Change to hover type
            if home_screen[cipher_type].hover == False:
                screen.blit(home_screen[cipher_type].images['button_hover'], (0,home_screen[cipher_type].button.y))
                home_screen[cipher_type].hover = True
                pygame_ess.update()

            # Check of click
            click(cipher_type)

            # Get new mouse position
            mouse_pos = pygame.mouse.get_pos()
            
        if home_screen[cipher_type].hover:
            screen.blit(home_screen[cipher_type].images['button'], (0,home_screen[cipher_type].button.y))
            home_screen[cipher_type].hover = False
            pygame_ess.update()
    

##
## Main loop
load_home_screen()

while True:
    selection()
    # Did the user click the window close button?
    pygame_ess.buffer()

# Done! Time to quit.
pygame.quit()
