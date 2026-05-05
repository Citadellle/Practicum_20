class Circle:
    '''
    A class representing a circle.

    Class Attributes:
        all_circles (list): List of all created Circle instances
        pi (float): A constant representing the value of pi.
    '''
    all_circles = []
    pi = 3.1415

    def __init__(self, radius = 1):
        '''
        Initialize a Circle instance and 
        adds the created instance to the `all_circles` list.

        Args:
            radius (float): The radius of the circle.
        '''
        self.radius = radius
        Circle.all_circles.append(self)
    
    def __str__(self):
        '''
        Returns a string representation of the circle.

        Returns:
            str: The radius of the circle as a string.
        '''
        return str(self.radius)
    
    def __repr__(self):
        '''
        Returns a developer-friendly string representation of the circle.

        Returns:
            str: The radius of the circle as a string.
        '''
        return str(self.radius)

    def area(self):
        '''
        Calculates the area of the circle.

        Returns:
            float: The area of the circle (pi * radius^2)
        '''
        return Circle.pi * self.radius ** 2
    
    @staticmethod
    def total_area():
        '''
        Calculates the total area of all created circles.

        Returns:
            float: The sum of areas of all circle instances
        '''
        s = 0
        for circle in Circle.all_circles:
            s += circle.area()
        return s