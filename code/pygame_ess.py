##
## Import and initialize the librarys
import pygame
import glob

##
## Essentials functions

class pygame_ess:
    
    def load_images(image_page=[], file_type='.png'):
        images = dict()
        image_dir = 'images/{}/'.format('/'.join(image_page))
        # Get all image file from givent directory
        image_dir_list = glob.glob(image_dir+"*"+file_type)

        # Load them into pygame
        for image in image_dir_list:
            image_name = image.split('/')[-1].split('.')[0]
            images[image_name] = pygame.image.load(image).convert()

        return images

    def load_screen(screen, screen_objects):
        # Load background
        screen.blit(screen_objects['background'].images['background'],  screen_objects['background'].frame.image_coord())

        # Load buttons items
        for screen_object in screen_objects.values():
            if screen_object.type == 'button':
                screen.blit(screen_object.images[screen_object.type], screen_object.frame.image_coord())
            elif screen_object.type in ['textfield', 'text']:
                screen.blit(screen_object.images['textfield'], screen_object.frame.image_coord())
                screen.blit(screen_object.meta.render_text(), screen_object.frame.box_coord())

        pygame_ess.update()

    def button_event(selection_object):
        for event in pygame.event.get():                
            # Check for left click
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                print("clicked", selection_object.name)

                if type(selection_object.runclass) == str: return selection_object.runclass

                # Load new screen
                try: 
                    runclass_result = selection_object.runclass.run()
                    return True
                except: print('error loading', selection_object.name)
                finally: return True

        return False

    def textfield_event(screen, selection_object):
        for event in pygame.event.get():                
            # Check for left click
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                textfield_result = selection_object.runclass.run(screen, selection_object)
                return textfield_result

        return False

    def selection(screen, selection_objects):

        for selection_object in selection_objects.values():

            object_type = selection_object.type

            while selection_object.in_box(pygame.mouse.get_pos()):
                if object_type == 'button': 
                    # Change to hover type
                    if selection_object.hover == False:
                        screen.blit(selection_object.images['button_hover'], (selection_object.frame.image_coord()))
                        selection_object.hover = True
                        pygame_ess.update()

                    # Check of click
                    button_result = pygame_ess.button_event(selection_object) 
                    if button_result != False: return {'button': button_result}

                elif object_type == 'textfield': 
                    textfield_result = pygame_ess.textfield_event(screen, selection_object) 
                    if textfield_result != False: return {'textfield': textfield_result}

                else: pygame_ess.buffer()

            # Moved out of hitbox
            if selection_object.hover:
                screen.blit(selection_object.images['button'], (selection_object.frame.image_coord()))
                selection_object.hover = False
                pygame_ess.update()

        return {'':''}
                

    def update(tick=120):
        pygame.display.flip()
        pygame.display.update()
        pygame.time.Clock().tick(tick)

    def buffer():
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return True
