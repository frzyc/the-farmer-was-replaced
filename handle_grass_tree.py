from move_drone import *
from plant_carrot import *
from water_tile import *
from globals import *


def handle_grass_tree():
    if can_harvest():
        harvest()
    x = get_pos_x()
    y = get_pos_y()
    if not plant_carrot():
        if (x + y) % 2 == 0 and num_items(Items.Wood):
            if get_ground_type() == Grounds.Turf:
                till()
            plant(Entities.Tree)
        else:
            # grass
            if get_ground_type() == Grounds.Soil:
                till()  # convert back to turf
