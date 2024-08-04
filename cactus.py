from globals import *
from water_tile import *
from move_drone import *
from plant_field import *


def cactus():
    size = get_world_size()
    buy_num = size * size
    while buy(Items.Cactus_Seed, buy_num) and num_items(Items.Cactus) < get_min(
        Items.Cactus
    ):
        clear()
        plant_field(Entities.Cactus)
        # switaroo
        while True:
            x = get_pos_x()
            y = get_pos_y()
            current = measure()

            # check north
            if y == size - 1:
                n = None
            else:
                n = measure(North)  # measure loops around map
            if n != None and (n < current):
                swap(North)
                current = n

            # check east
            if x == size - 1:
                e = None
            else:
                e = measure(East)  # measure loops around map
            if e != None and (e < current):
                swap(East)
                current = e

            # check west
            if x == 0:
                w = None
            else:
                w = measure(West)  # measure loops around map
            if w != None and (w > current):
                swap(West)
                move(West)
                continue

            # check south
            if y == 0:
                s = None
            else:
                s = measure(South)  # measure loops around map
            if s != None and (s > current):
                swap(South)
                move(South)
                continue

            move_drone()
            if get_pos_x() == 0 and get_pos_y() == 0:
                break
        harvest()
        # harvest
    return False
