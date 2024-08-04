from globals import *
from water_tile import *


def plant_pumpkin():
    if get_entity_type() == Entities.Pumpkin:
        if can_harvest() and get_pos_x() == 0 and get_pos_y() == 0:
            harvest()
        return True
    if num_items(Items.Pumpkin_Seed) <= 0:
        # buy
        buy_num = get_world_size() * get_world_size() * 10
        if num_items(Items.Carrot) < (buy_num + get_min_carrots()):
            return False
        trade(Items.Pumpkin_Seed, buy_num)

    # should have seeds
    if get_ground_type() != Grounds.Soil:
        till()
    while get_entity_type() != Entities.Pumpkin and not can_harvest():
        if not num_items(Items.Pumpkin_Seed):
            return False
        plant(Entities.Pumpkin)
        water_tile()

    return True
