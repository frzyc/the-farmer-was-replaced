def move_maze(dir):
    x = get_pos_x()
    y = get_pos_y()
    move(dir)
    return x == get_pos_x() and y == get_pos_y()
