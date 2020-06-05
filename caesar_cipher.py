##
## Import and initialize the librarys
import pygame
from image_storage import *
from pygame_ess import pygame_ess


##
## Initialization
pygame.init()

# Set up the drawing window
window_size = (1024, 768)
screen = pygame.display.set_mode((1024, 768))
window = pygame.surface.Surface((window_size))
pygame.display.set_caption("Caesar Cipher")


##
## Variables
image_dir = 'images/caesar_cipher/'
button_types = ['back', 'info'] 
caesar_cipher_screen = dict()


##
## Load home screen images

# background image
caesar_cipher_screen['background'] = pygame_ess.load_images(image_dir)

# Buttons
for button_type in button_types:
    caesar_cipher_screen[button_type] = image_item(button_type,
                                      pygame_ess.load_images(image_dir+button_type+'/'),
                                      coord(47 + 766 * button_types.index(button_type), 28, 162, 67))


##
## 
class caesar_cipher:

    def load_caesar_cipher():
        screen.blit(caesar_cipher_screen['background']['caesar_cipher_bg'], (0,0))
        
        pygame_ess.update()
    
    def run():
        caesar_cipher.load_caesar_cipher()
        
        while True:
            if pygame_ess.buffer(): break
            
