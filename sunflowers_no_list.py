from globals import *
from water_tile import *
from move_drone import *
from move_to import *

# Solution for sunflower without using lists. use sunflower_list once lists are unlocked.


def sunflowers_no_list():
    # start at 0,0
    if get_pos_x() != 0 or get_pos_y() != 0:
        return False

    cost = get_cost(Items.Sunflower_Seed)
    carr_cost = cost[Items.Carrot]
    # buy
    buy_num = get_world_size() * get_world_size() * 10
    if num_items(Items.Sunflower_Seed) <= buy_num:
        if num_items(Items.Carrot) < (buy_num * carr_cost + get_min_carrots()):
            return False
        trade(Items.Sunflower_Seed, buy_num)

    clear()
    # plant
    while True:
        if get_ground_type() != Grounds.Soil:
            till()
        water_tile()
        plant(Entities.Sunflower)
        move_drone()
        if get_pos_x() == 0 and get_pos_y() == 0:
            break

    while True:
        # check pedals
        highest_pedal = 0
        num_sunflow = 0
        harvested = False
        while True:
            if get_entity_type() == Entities.Sunflower:
                while not can_harvest():
                    water_tile()
                num_sunflow += 1
                current = measure()
                if current == 15:
                    harvest()
                    plant(Entities.Sunflower)
                    move_to(0, 0)
                    harvested = True
                    break
                if current > highest_pedal:
                    highest_pedal = current
            move_drone()
            if get_pos_x() == 0 and get_pos_y() == 0:
                break
        if harvested:
            continue
        if not num_sunflow:
            break
        # harvest
        while True:
            current = measure()
            if current == highest_pedal:
                harvest()
                plant(Entities.Sunflower)
                move_to(0, 0)
                break
            move_drone()
            if get_pos_x() == 0 and get_pos_y() == 0:
                break

    return True
