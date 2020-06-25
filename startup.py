################
# Startup file #
################

######################################
# Import and initialize the librarys #
######################################
import sys
import os
import logging
import logging.handlers
from datetime import datetime

# Set to code directory
sys.path.insert(1, './code')


#####################
# Get configuration #
#####################
from config import config


#######################
# Setup debug logging #
#######################

# Ensure that logs folder is created
if not os.path.isdir('./logs'):
    # Create logs directory
    try: os.mkdir('logs')
    except OSError: print("[ERROR] Creation of the directory ./logs failed")
    else: print("[INFO] Successfully created the directory ./logs")

# Get date
# datetime object containing current date and time
now = datetime.now()
# Convert to file dir
log_file_dir = now.strftime("./logs/%d-%m-%Y_%H-%M-%S_debug.log")

# Change root logger level from WARNING (default) to NOTSET in order for all messages to be delegated.
logging.getLogger().setLevel(logging.NOTSET)

# Add stdout handler, with level INFO
console = logging.StreamHandler(sys.stdout)
console.setLevel(level=os.environ.get("LOGLEVEL", config.debug_level.console))
formater = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', datefmt='%H:%M:%S')
console.setFormatter(formater)
logging.getLogger().addHandler(console)

# Add file debug handler, with level DEBUG
debugHandler = logging.handlers.RotatingFileHandler(filename=log_file_dir, mode='w')
debugHandler.setLevel(level=os.environ.get("LOGLEVEL", config.debug_level.logs))
formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', datefmt='%H:%M:%S')
debugHandler.setFormatter(formatter)
logging.getLogger().addHandler(debugHandler)


#################################
# Starting Cryptography GUI app #
#################################
if __name__ == "__main__":
    logging.info('Starting Crpytography GUI...')
    logging.info(config)

    # Initialize pygame
    from pygame_ess import pygame_ess
    from home_screen import cryptography

    # Run home screen
    pygame_ess.set_caption('Cryptography GUI')
    cryptography.run()

    # End program
    pygame_ess.quit()