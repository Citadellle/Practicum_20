import re

class RomanNumber:
    '''
    A class representing a Roman numeral with bidirectional conversion.
    Supports conversion from Roman to decimal and decimal to Roman,
    as well as arithmetic operations.
    '''

    def __init__(self, value):
        '''
        Initializes a new RomanNumber instance.

        Args:
            value (str or int): Either a Roman numeral string or an integer
        
        Note:
            If the value is invalid, rom_value and int_value are set to None
            and 'ошибка' is printed.
        ''' 
        self.rom_value = None
        self.int_value = None

        if isinstance(value, str):
            if self.is_roman(value):
                self.rom_value = value
                self.int_value = self.decimal_number()
            else:
                print('ошибка')
        
        elif isinstance(value, int):
            if self.is_int(value):
                self.int_value = value
                self.rom_value = self.roman_number()
            else:
                print('ошибка')
        
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

        result_dec = 0
        last_num = 0
        
        for char in self.rom_value[::-1]:
            decimal_num = roman_nums[char]
            if decimal_num < last_num:
                result_dec -= decimal_num
            else:
                result_dec += decimal_num
            
            last_num = decimal_num

        return result_dec
    
    def roman_number(self):
        '''
        Converts the decimal integer to its Roman numeral equivalent.

        Returns:
            str: The Roman numeral string, or None if the integer is invalid
        '''      
        if self.int_value is None:
            return None
        
        roman_nums = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]

        value = self.int_value
        result_rom = ''

        while value > 0:
            for num, letter in roman_nums:
                while value >= num:
                    result_rom += letter
                    value -= num
                
        return result_rom
    
    @staticmethod
    def is_roman(value):
        '''
        Checks if a string is a valid Roman numeral.

        Args:
            value (str): The string to check

        Returns:
            bool: True if the string is a valid Roman numeral, False otherwise
        '''
        if isinstance(value, str):
            pattern = re.compile(r'^(M{0,3})(D?C{0,3}|C[DM])(L?X{0,3}|X[LC])(V?I{0,3}|I[VX])$')
            return bool(re.fullmatch(pattern, value))
        
        return False
    
    @staticmethod
    def is_int(value):
        '''
        Checks if an integer is within the valid range for Roman numerals.

        Args:
            value (int): The integer to check

        Returns:
            bool: True if the integer is between 1 and 3999 inclusive, False otherwise
        '''
        if isinstance(value, int):
            if 1 <= value <= 3999:
                return True
            
        return False
    
    def __add__(self, other): # +
        '''
        Sum two Roman numbers and returns a new RomanNumber.

        Args:
            other (RomanNumber): The other Roman number to sum

        Returns:
            RomanNumber: A new RomanNumber representing the sum,
                        or RomanNumber(-1) if the result is invalid
        '''
        if isinstance(self, RomanNumber) and isinstance(other, RomanNumber):
            if self.int_value is not None and other.int_value is not None:
                value_1, value_2 = self.int_value, other.int_value

                result = value_1 + value_2
                if 1 <= result <= 3999:
                    return RomanNumber(result)
                
        return RomanNumber(-1)
    
    def __sub__(self, other): # - 
        '''
        Subtracts one Roman number from another.

        Args:
            other (RomanNumber): The Roman number to subtract

        Returns:
            RomanNumber: A new RomanNumber representing the difference,
                        or RomanNumber(-1) if the result is invalid
        '''
        if isinstance(self, RomanNumber) and isinstance(other, RomanNumber):
            if self.int_value is not None and other.int_value is not None:
                value_1, value_2 = self.int_value, other.int_value

                result = value_1 - value_2
                if 1 <= result <= 3999:
                    return RomanNumber(result)
                
        return RomanNumber(-1)
    
    def __mul__(self, other): # *
        '''
        Multiplies two Roman numbers.

        Args:
            other (RomanNumber): The other Roman number to multiply by

        Returns:
            RomanNumber: A new RomanNumber representing the product,
                        or RomanNumber(-1) if the result is invalid
        '''
        if isinstance(self, RomanNumber) and isinstance(other, RomanNumber):
            if self.int_value is not None and other.int_value is not None:
                value_1, value_2 = self.int_value, other.int_value

                result = value_1 * value_2
                if 1 <= result <= 3999:
                    return RomanNumber(result)
                
        return RomanNumber(-1)
    
    def __truediv__(self, other): # /
        '''
        Divides one Roman number by another.

        Args:
            other (RomanNumber): The divisor

        Returns:
            RomanNumber: A new RomanNumber representing the quotient,
                        or RomanNumber(-1) if division is not exact
                        or the result is invalid
        '''
        if isinstance(self, RomanNumber) and isinstance(other, RomanNumber):
            if self.int_value is not None and other.int_value is not None:
                value_1, value_2 = self.int_value, other.int_value

                if value_1 % value_2 == 0:
                    result = value_1 / value_2
                    if 1 <= result <= 3999:
                        return RomanNumber(int(result))
                    
        return RomanNumber(-1)
    
    def __floordiv__(self, other): # //
        '''
        Performs integer division of one Roman number by another.

        Args:
            other (RomanNumber): The divisor

        Returns:
            RomanNumber: A new RomanNumber representing the integer quotient,
                        or RomanNumber(-1) if the result is invalid
        '''
        if isinstance(self, RomanNumber) and isinstance(other, RomanNumber):
            if self.int_value is not None and other.int_value is not None:
                value_1, value_2 = self.int_value, other.int_value

                result = value_1 // value_2
                if 1 <= result <= 3999:
                    return RomanNumber(result)
                
        return RomanNumber(-1)
    
    def __mod__(self, other): # %
        '''
        Returns the remainder of division of one Roman number by another.

        Args:
            other (RomanNumber): The divisor

        Returns:
            RomanNumber: A new RomanNumber representing the remainder,
                        or RomanNumber(-1) if the result is invalid
        '''
        if isinstance(self, RomanNumber) and isinstance(other, RomanNumber):
            if self.int_value is not None and other.int_value is not None:
                value_1, value_2 = self.int_value, other.int_value

                result = value_1 % value_2
                if 1 <= result <= 3999:
                    return RomanNumber(result)
                
        return RomanNumber(-1)

    def __pow__(self, other): # **
        '''
        Raises one Roman number to the power of another.

        Args:
            other (RomanNumber): The exponent

        Returns:
            RomanNumber: A new RomanNumber representing the power result,
                        or RomanNumber(-1) if the result is invalid
        '''
        if isinstance(self, RomanNumber) and isinstance(other, RomanNumber):
            if self.int_value is not None and other.int_value is not None:
                value_1, value_2 = self.int_value, other.int_value

                result = value_1 ** value_2
                if 1 <= result <= 3999:
                    return RomanNumber(result)
                
        return RomanNumber(-1)