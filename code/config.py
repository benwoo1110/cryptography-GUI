######################################
# Import and initialize the librarys #
######################################
import yaml
import os

##########################
# Getting configurations #
##########################

# Default setting for file
default_config_contents = '''\
# NOTE: Change only if you know what you are doing!

# Size of pygame window in pixel
screen_size:
  width: 768
  height: 1024

# Level of output shown
debug_level:
  console: 'INFO'
  logs: 'DEBUG'
'''

# Set config file directory
config_dir = './config.yml'
if os.path.basename(os.getcwd()) == 'code': config_dir = '../config.yml'

# Create file if it doesnt exist
if not os.path.isfile(config_dir):
    with open(config_dir, 'w') as config_file:
        config_file.write(default_config_contents)

# Read from config file
with open(config_dir) as config_file:
        parsed_config_file = yaml.load(config_file, Loader=yaml.FullLoader)
        config_file.close()


###############
# For testing #
###############
if __name__ == "__main__":
    print(parsed_config_file)