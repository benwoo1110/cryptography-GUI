# This file is part of Cryptography GUI, licensed under the MIT License.
# Copyright (c) 2020 Benedict Woo Jun Kai
# See LICENSE.md for more details.


######################################
# Import and initialize the librarys #
######################################
import logging
from invalid_input import invalid_input

logging.info('Loading input validation checks...')


#############################
# Input validation function #
#############################
class validate:

    class text:
        def __init__(self, max_length:int = 30, chars_allowed:list = None, use_ascii:bool = True):
            self.max_length:int = max_length
            self.chars_allowed:list = chars_allowed
            self.use_ascii:bool = use_ascii

            # Use default text
            if chars_allowed == None:
                # All letters, numbers and symbols in ASCII
                self.chars_allowed = list(range(32,65)) + list(range(91,127)) + [8]


        def check(self, text:str) -> bool:
            # Check if text exceed max length
            if len(text) > self.max_length: 
                invalid_input.run()
                return False

            # Check if each char in chars_allowed
            for char in text.lower():
                if self.use_ascii:
                    if ord(char) not in self.chars_allowed: 
                        invalid_input.run('Text should only contain text, numbers and symbols')
                        return False
                else:
                    if char not in self.chars_allowed: 
                        invalid_input.run('Text should only contain text, numbers and symbols')
                        return False
                
            # If check is all satisfied
            return True


    class digits:
        def __init__(self, max_length:int = 6, chars_allowed:list = None, min_num:float = 0, max_num:float = 999999,  use_ascii:bool = True, is_float:bool = False):
            self.max_length:int = max_length
            self.chars_allowed:list = chars_allowed
            self.min_num:float = min_num
            self.max_num:float = max_num
            self.use_ascii:bool = use_ascii
            self.is_float:bool = is_float

            # Use default numbers
            if chars_allowed == None:
                # All numbers and backspace
                self.chars_allowed = list(range(48,58)) + [8]
                # Add . if number is float
                if is_float: self.chars_allowed.append(46)
                # Add - if min_num can be negative
                if min_num < 0: self.chars_allowed.append(45)

        def num_range(self) -> range:
            return range(self.min_num, self.max_num+1)

        def check(self, number:str) -> bool:
            # Check if doesnt exceed max_length
            if len(number) > self.max_length: 
                invalid_input.run('Text exceeded max length of {} characters'.format(self.max_length))
                return False

            # Check if its a float
            if self.is_float:
                try: check_number = int(number)
                except: 
                    invalid_input.run('Input is not an integer from {} to {}.'.format(self.min_num, self.max_num))
                    return False       
                
            # Check if its a integer
            else:
                try: 
                    check_number = int(number)
                except: 
                    invalid_input.run('Input is not an float from {} to {}.'.format(self.min_num, self.max_num))
                    return False
            
            # Checks if number is in range
            if check_number not in self.num_range():
                invalid_input.run('Input number need to be between {} and {}.'.format(self.min_num, self.max_num))
                return False

            return True