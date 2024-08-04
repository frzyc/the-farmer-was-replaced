def move_drone():
    if get_pos_x() == get_world_size() - 1:
        move(North)
    move(East)
