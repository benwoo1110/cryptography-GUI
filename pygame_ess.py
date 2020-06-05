##
## Import and initialize the librarys
import pygame
import glob

class pygame_ess:
    
    def load_images(image_dir='images/', file_type='.png'):
        images = dict()
        # Get all image file from givent directory
        image_dir_list = glob.glob(image_dir+"*"+file_type)

        # Load them into pygame
        for image in image_dir_list:
            image_name = image.split('/')[-1].split('.')[0]
            images[image_name] = pygame.image.load(image).convert()

        return images

    def update(tick=1000000000):
        pygame.display.flip()
        pygame.display.update()
        pygame.time.Clock().tick(tick)

    def buffer():
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit()

    