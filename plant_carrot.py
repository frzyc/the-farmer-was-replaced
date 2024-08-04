from globals import *
from water_tile import *


def plant_carrot():
    if get_entity_type() == Entities.Carrots:
        return True
    if num_items(Items.Carrot_Seed) <= 0:
        buy_num = get_world_size() * get_world_size() * 2
        if num_items(Items.Hay) < (buy_num + get_min_hay()) or num_items(Items.Wood) < (
            buy_num + get_min_wood()
        ):
            return False
        else:
            trade(Items.Carrot_Seed, buy_num)
    if get_ground_type() != Grounds.Soil:
        till()
    plant(Entities.Carrots)
    water_tile()
    return True
