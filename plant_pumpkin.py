from globals import *
from water_tile import *
from move_drone import *


# General pumpkin logic without using lists.
def plant_pumpkin():
    buy_num = get_world_size() * get_world_size() * 10
    if not buy(Items.Pumpkin_Seed, buy_num):
        return False
    clear()
    while True:
        if get_entity_type() == Entities.Pumpkin:
            if can_harvest() and get_pos_x() == 0 and get_pos_y() == 0:
                harvest()

        # should have seeds
        if get_ground_type() != Grounds.Soil:
            till()
        while get_entity_type() != Entities.Pumpkin and not can_harvest():
            if not num_items(Items.Pumpkin_Seed):
                return False
            plant(Entities.Pumpkin)
            water_tile()
        move_drone()
    return True
