import re

class RomanNumber:
    '''
    A class representing a Roman numeral.
    Provides validation, string representation, and conversion to decimal.

    Attributes:
        rom_value (str): The Roman numeral string (None if invalid)
    '''

    def __init__(self, value):
        '''
        Initializes a new RomanNumber instance.

        Args:
            value (str): The Roman numeral string
        
        Note:
            If the value is not a valid Roman numeral, rom_value is set to None
            and 'ошибка' is printed.
        '''        
        self.rom_value = None

        if self.is_roman(value):
            self.rom_value = value
        else:
            print('ошибка')

    def __str__(self):
        '''
        Returns a string representation of the Roman numeral.

        Returns:
            str: The Roman numeral string
        '''
        return str(self.rom_value)
    
    def __repr__(self):
        '''
        Returns a developer-friendly string representation.

        Returns:
            str: The Roman numeral string
        '''
        return str(self.rom_value)
    
    def decimal_number(self):
        '''
        Converts the Roman numeral to its decimal (integer) equivalent.

        Returns:
            int: The decimal value of the Roman numeral,
                 or None if the Roman numeral is invalid
        '''
        if self.rom_value is None:
            return None
        
        roman_nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        result = 0
        last_num = 0
        
        for char in self.rom_value[::-1]:
            decimal_num = roman_nums[char]
            if decimal_num < last_num:
                result -= decimal_num
            else:
                result += decimal_num
            
            last_num = decimal_num

        return result
    
    @staticmethod
    def is_roman(value):
        '''
        Checks if a string is a valid Roman numeral.

        Args:
            value (str): The string to check

        Returns:
            bool: True if the string is a valid Roman numeral, False otherwise
        '''
        if not isinstance(value, str):
            return False
        pattern = re.compile(r'^(M{0,3})(D?C{0,3}|C[DM])(L?X{0,3}|X[LC])(V?I{0,3}|I[VX])$')
        # Check for a full match with the all string
        return bool(re.fullmatch(pattern, value))