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
        match NavalBattle.playing_field[y][x]:
            case 1:
                print('попал')
                NavalBattle.playing_field[y][x] = self.symbol

            case 0:
                print('мимо')
                NavalBattle.playing_field[y][x] = 'o'