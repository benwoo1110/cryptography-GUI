##
## Import and initialize the librarys
import pygame
import glob

##
## Essentials functions
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

    def click_event(selection_type, runclass):
        for event in pygame.event.get():
            # Check for left click
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Load cipher screen
                print("clicked", selection_type)
                runclass.run()

                return True

    def selection(screen, current_screen, selection_types):
        mouse_pos = pygame.mouse.get_pos()

        for selection_type in selection_types.keys():
            while current_screen[selection_type].in_box(mouse_pos):
                # Change to hover type
                if current_screen[selection_type].hover == False:
                    screen.blit(current_screen[selection_type].images['button_hover'], (current_screen[selection_type].button.image_coord()))
                    current_screen[selection_type].hover = True
                    pygame_ess.update()

                # Check of click
                if pygame_ess.click_event(selection_type, selection_types[selection_type]): 
                    return True

                # Get new mouse position
                mouse_pos = pygame.mouse.get_pos()
                
            if current_screen[selection_type].hover:
                screen.blit(current_screen[selection_type].images['button'], (current_screen[selection_type].button.image_coord()))
                current_screen[selection_type].hover = False
                pygame_ess.update()
    

    def update(tick=1000000000):
        pygame.display.flip()
        pygame.display.update()
        pygame.time.Clock().tick(tick)

    def buffer():
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return True

    
