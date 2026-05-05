import random

class NavalBattle:
    '''
    A class representing a Naval Battle game.
    Manages the playing field, process shots, 
    and displays the current state of the game.

    Class Attributes:
        playing_field (list): list representing the game board.
                              0 - empty cell, 1 - ship cell
    '''
    playing_field  = []

    def __init__(self, symbol):
        '''
        Initializes a new NavalBattle instance.

        Args:
            symbol (str): The symbol to mark broke ships.
        '''
        self.symbol = symbol

    @staticmethod
    def show():
        '''
        Displays the current state of the playing field.
        Hidden cells (0 and 1) are shown as '~',
        hit markers and misses are shown as their appropriate symbols.
        '''
        for row in NavalBattle.playing_field:
            display_row = []

            for el in row:
                if el == 0 or el == 1:
                    display_row.append('~')

                else:
                    display_row.append(el)
                
            print(*display_row)

    def shot(self, x, y):
        '''
        Processes a shot at the specified coordinates.

        Args:
            x (int): X-coordinate of the shot
            y (int): Y-coordinate of the shot
        '''
        x -= 1
        y -= 1

        try:
            match NavalBattle.playing_field[y][x]:
                case 1:
                    print('попал')
                    NavalBattle.playing_field[y][x] = self.symbol

                case 0:
                    print('мимо')
                    NavalBattle.playing_field[y][x] = 'o'

                case _:
                    print('ошибка')
        except:
            print('игровое поле не заполнено')
    
    @classmethod
    def new_game(cls):
        '''
        Creates a new game by random placing ships on a 10x10 board.
        
        Ship configuration:
        - 1 four-deck ship
        - 2 three-deck ships
        - 3 double-deck ships
        - 4 single-deck ships     
        
        Ships are placed randomly with validation to ensure they don't touch
        each other. 
        If placement fails after 1000 attempts, the method calls itself again.
        '''
        ships = [(1, 4), (2, 3), (3, 2), (4, 1)]
        available_cells = [(x, y) for x in range(10) for y in range(10)]
        field = [[0 for _ in range(10)] for _ in range(10)]


        def delete_environment_of_cell(available_cells, x_0, y_0):
            '''
            Removes the cell and all its neighboring cells
            from the available cells list.

            Args:
                available_cells (list): List of available coordinates
                x (int): X-coordinate of the cell
                y (int): Y-coordinate of the cell
            '''
            for dx in range(-1, 1 + 1):
                for dy in range(-1, 1 + 1):
                    x, y = x_0 + dx, y_0 + dy

                    try:
                        available_cells.remove((x, y))

                    except:
                        continue


        for length, count in ships:
            for _ in range(count):
                placed = False
                attempt = 1

                while not placed and attempt < 1000:

                    orientation = random.randint(0, 1)

                    match orientation:
                        # Horizontally
                        case 0:
                            x = random.randint(0, 10 - length)
                            y = random.randint(0, 9)
                            cells = [(x + i, y) for i in range(length)]

                        # Vertically
                        case 1:
                            x = random.randint(0, 9)
                            y = random.randint(0, 10 - length)
                            cells = [(x, y + i) for i in range(length)]
                    
                    if all(cell in available_cells for cell in cells):
                        for x, y in cells:
                            field[y][x] = 1
                            delete_environment_of_cell(available_cells, x, y)
                        placed = True
                    
                    attempt += 1
                
                if not placed:
                    cls.new_game()

        NavalBattle.playing_field = field
