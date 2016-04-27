def get_row_col(chip_location):
    """Gets chip location as a parameter
    Returns raw row and col
    """
    return chip_location.split()[1], chip_location.split()[0].upper()


def get_row_col_literals(chip_location):
    """Gets chip location as a parameter.
    Returns literal row and col position as a tuple
    """
    row = int(get_row_col(chip_location)[0]) - 1
    col = ord(get_row_col(chip_location)[1]) - 65
    return row, col
