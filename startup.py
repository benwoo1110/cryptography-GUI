################
# Startup file #
################

######################################
# Import and initialize the librarys #
######################################
import pygame
# Set to code directory
import sys
sys.path.insert(1, './code')


#######################
# Setup debug logging #
#######################
import logging
import logging.handlers
from datetime import datetime

# Get date
# datetime object containing current date and time
now = datetime.now()
# Convert to file dir
log_file_dir = now.strftime("./logs/%d-%m-%Y_%H-%M-%S_debug.log")

# Change root logger level from WARNING (default) to NOTSET in order for all messages to be delegated.
logging.getLogger().setLevel(logging.NOTSET)

# Add stdout handler, with level INFO
console = logging.StreamHandler(sys.stdout)
console.setLevel(logging.INFO)
formater = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', datefmt='%H:%M:%S')
console.setFormatter(formater)
logging.getLogger().addHandler(console)

# Add file debug handler, with level DEBUG
debugHandler = logging.handlers.RotatingFileHandler(filename=log_file_dir, mode='w')
debugHandler.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', datefmt='%H:%M:%S')
debugHandler.setFormatter(formatter)
logging.getLogger().addHandler(debugHandler)


#################################
# Starting Cryptography GUI app #
#################################
if __name__ == "__main__":
    logging.info('Starting Crpytography GUI...')
    
    # Initialize pygame
    pygame.init()
    pygame.display.set_caption("Cryptography GUI")

    # Run home screen
    from home_screen import cryptography
    cryptography.run()

    # End program
    logging.info('Exiting program...')
    pygame.quit()