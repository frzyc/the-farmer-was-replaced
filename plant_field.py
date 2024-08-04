from water_tile import *
from move_drone import *


def plant_field(entity):
    while True:
        if get_ground_type() != Grounds.Soil:
            till()
        water_tile()
        plant(entity)
        move_drone()
        if get_pos_x() == 0 and get_pos_y() == 0:
            break
