def config_size(ROWS,COLUMNS,WIDTH_CELL,HEIGHT_CELL,MARGIN,SCREEM_WIDTH,SCREEM_HEIGHT,CHARACTER_SCALING):
    ROWS = 8
    COLUMNS = 8
    WIDTH_CELL = 80
    HEIGHT_CELL = 80
    MARGIN = 5
    SCREEM_WIDTH = (WIDTH_CELL + MARGIN) * ROWS + MARGIN
    SCREEM_HEIGHT = (HEIGHT_CELL + MARGIN) * COLUMNS + MARGIN
    CHARACTER_SCALING = 0.6
    return ROWS, COLUMNS, WIDTH_CELL, HEIGHT_CELL, MARGIN, SCREEM_WIDTH, SCREEM_HEIGHT, CHARACTER_SCALING