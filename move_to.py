def move_to(x, y):
    cx = get_pos_x()
    cy = get_pos_y()
    wsize = get_world_size()
    if x != cx:
        east = x - cx
        if east < 0:
            east = east + wsize
        west = cx - x
        if west < 0:
            west = west + wsize
        if east < west:
            for i in range(east):
                move(East)
        else:
            for i in range(west):
                move(West)
    if y != cy:
        north = y - cy
        if north < 0:
            north = north + wsize
        south = cy - y
        if south < 0:
            south = south + wsize
        if north < south:
            for i in range(north):
                move(North)
        else:
            for i in range(south):
                move(South)
