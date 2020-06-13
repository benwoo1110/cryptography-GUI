class input_validation:

    class text:
        def __init__(self, max_length:int = 30, chars_allowed:list = None, use_ascii:bool = True):
            self.max_length = max_length
            self.chars_allowed = chars_allowed
            self.use_ascii = use_ascii

            # Use default text
            if chars_allowed == None:
                # All letters, numbers and symbols in ASCII
                self.chars_allowed = list(range(32,65)) + list(range(91,127)) + [8]


        def validate(self, text):
            # Check if text exceed max length
            if len(text) > self.max_length: return False

            # Check if each char in chars_allowed
            for char in text.lower():
                if ord(char) not in self.chars_allowed: return False
                
            # If check is all satisfied
            return True


    class digits:
        def __init__(self, chars_allowed:list = None, min_num:float = 0, max_num:float = 999999,  use_ascii:bool = True, is_float:bool = False):
            self.chars_allowed = chars_allowed
            self.min_num = min_num
            self.max_num = max_num
            self.use_ascii = use_ascii
            self.is_float = is_float

            # Use default numbers
            if chars_allowed == None:
                # All numbers and backspace
                self.chars_allowed = list(range(48,58)) + [8]
                # Add . if number is float
                if is_float: self.chars_allowed.append(46)


        def num_range(self):
            return range(self.min_num, self.max_num+1)

        def validate(self, number):
            # Check if its a float
            if self.is_float:
                try: check_number = int(number)
                except: 
                    print('Text not a Integer.')
                    return False       
                
            # Check if its a integer
            else:
                try: check_number = int(number)
                except: 
                    print('Text not a Integer.')
                    return False
            
            # Checks if number is in range
            if check_number in self.num_range():
                return True

            return False