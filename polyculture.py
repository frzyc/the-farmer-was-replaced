from move_drone import *
from globals import *
from water_tile import *


def polyculture():
    clear()
    # start at 0,0
    if get_pos_x() != 0 or get_pos_y() != 0:
        return False

    # create an array2 to store entities
    grid = get_grid(Entities.Grass)

    # else grow grass
    while True:
        if can_harvest():
            harvest()
        x = get_pos_x()
        y = get_pos_y()

        # check inventory
        if x == 0 and y == 0:
            if (
                num_items(Items.Carrot) > get_min_carrots() * 2
                and num_items(Items.Wood) > get_min_wood() * 2
                and num_items(Items.Hay) > get_min_hay() * 2
            ):
                break

        companion = grid[x][y]
        if companion == Entities.Carrots and num_items(Items.Carrot_Seed) == 0:
            trade(Items.Carrot_Seed, 100)
        if companion == Entities.Grass and get_ground_type() == Grounds.Soil:
            till()
        else:
            if get_ground_type() == Grounds.Turf:
                till()
            plant(companion)
            water_tile()

        companion = get_companion()
        grid[companion[1]][companion[2]] = companion[0]

        move_drone()
    return True
