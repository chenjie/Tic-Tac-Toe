import math

EMPTY = '-'

def is_between(value, min_value, max_value):
    """ (number, number, number) -> bool

    Precondition: min_value <= max_value

    Return True if and only if value is between min_value and max_value,
    or equal to one or both of them.

    >>> is_between(1.0, 0.0, 2)
    True
    >>> is_between(0, 1, 2)
    False
    """
   
    # Students are to complete the body of this function, and then put their
    # solutions for the other required functions below this function.
    
    return value >= min_value and value <= max_value


def game_board_full(game_board):
    """ (str) -> bool
    
    Return True if and only if there are no EMPTY characters in the game board.
    
    >>> game_board_full('XOXOXOOXO')
    True
    >>> game_board_full('XOX-')
    False
    """
    
    return not(EMPTY in game_board)


def get_board_size(game_board):
    """ (str) -> int
    
    Precondition: The length of the game_board must be a perfect square, 
                  which is between 1 and 81 inclusive.
    
    Return the length of each side of the given 
    tic-tac-toe game board.
    
    >>> get_board_size('XXOO')
    2
    >>> get_board_size('XOOXOXXOX')
    3
    """
    
    return int(math.sqrt(len(game_board)))
    
    
def make_empty_board(board_size):
    """ (int) -> str
    
    Precondition: 1 <= board_size <= 9
    
    Return a string for storing information about a tic-tac-toe 
    game board whose size is given by the parameter.
    
    >>> make_empty_board(2)
    '----'
    >>> make_empty_board(3)
    '---------'
    """
    
    return EMPTY * board_size ** 2


def get_position(row_index, col_index, board_size):
    """ (int, int, int) -> int
    
    Precondition: 0 < row_index <= board_size and
                  0 < col_index <= board_size and
                  1 <= board_size <= 9
    
    Return the str_index of the cell in the string representation 
    of the game board corresponding to the given row and column indices.
    
    >>> get_position(2, 1, 4)
    4
    >>> get_position(3 ,1, 3)
    6
    """
    
    return (row_index - 1) * board_size + col_index - 1 


def make_move(player_symbol, row_index, col_index, game_board):
    """ (str, int, int, str) -> str
    
    Precondition: The row and col numbers must satisfy your 
                  input game_board size.
    
    Return the tic-tac-toe game board that 
    results when the given symbol is placed at the 
    given cell position in the given tic-tac-toe game board.
    
    >>> make_move('X', 2, 1, '----')
    '--X-'
    >>> make_move('O', 3, 1, '---------')
    '------O--'
    """
    
    # Calculate the index number of the input position.
    str_index = get_position(row_index, col_index, get_board_size(game_board))
    
    # Slice the string into two parts, not including the character 
    # of the input position.
    before = game_board[:str_index]
    after = game_board[(str_index + 1):]
    
    # Combine the three strings.
    return before + player_symbol + after


def extract_line(game_board, direction, row_or_column_number = None):
    """ (str, str[, int]) -> str
    
    Precondition: 0 < row_or_column_number <= 9
                  Directions: 'down', 'across', 'down_diagonal' 
                                                or 'up_diagonal'.
    
    Return the characters that make up the specified 
    row (when the second parameter is 'across'), 
    column (when the second parameter is 'down') or 
    diagonal from the given tic-tac-toe game board.
    When the second parameter is 'down_diagonal' or 'up_diagonal', 
    the value of the third parameter should not be used, since the 
    'down_diagonal' is known to start in the upper-left corner of 
    the game_board, and the 'up_diagonal' is known to start in the 
    lower-left corner of the game_board.
    
    >>> extract_line('XXOX', 'down', 1)
    'XO'
    >>> extract_line('XOOXOXOXX', 'down_diagonal')
    'XOX'
    """
    
    # Get the board size.
    board_size = get_board_size(game_board)
    
    # The following four if statements evaluate the four input situations.
    
    if len(game_board) == 1:
        return game_board
    
    elif direction == 'down':
        return game_board[row_or_column_number - 1::board_size]
    
    elif direction == 'across':
        return game_board[board_size * (row_or_column_number - 1):board_size 
                          * (row_or_column_number - 1) + board_size]
    
    elif direction == 'down_diagonal':
        return game_board[::board_size + 1]
    
    else:
        return game_board[pow(board_size, 2) - board_size: 0 :-(board_size - 1)]

# END