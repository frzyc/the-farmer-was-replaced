from globals import *
from water_tile import *
from move_drone import *
from move_to import *


def sunflower_list():
    # buy
    buy_num = get_world_size() * get_world_size() * 10
    if not buy(Items.Sunflower_Seed, buy_num):
        return False
    clear()
    grid = get_grid(0)
    # plant
    while True:
        if get_ground_type() != Grounds.Soil:
            till()
        water_tile()
        plant(Entities.Sunflower)
        move_drone()
        if get_pos_x() == 0 and get_pos_y() == 0:
            break

    # population grid with measurements
    while True:
        x = get_pos_x()
        y = get_pos_y()
        if get_entity_type() == Entities.Sunflower:
            while not can_harvest():
                water_tile()
                use_item(Items.Fertilizer)

            current = measure()
            if current == 15:
                current = harvest_and_measure()
            grid[x][y] = current
        move_drone()
        if get_pos_x() == 0 and get_pos_y() == 0:
            break

    # iterate through grid for highest pedal
    while True:
        highest_pedal = 0
        highest_x = 0
        highest_y = 0
        size = get_world_size()
        for x in range(size):
            for y in range(size):
                if grid[x][y] > highest_pedal:
                    highest_pedal = grid[x][y]
                    highest_x = x
                    highest_y = y
        if highest_pedal == 0:
            break
        move_to(highest_x, highest_y)
        highest_pedal = harvest_and_measure()
        grid[highest_x][highest_y] = highest_pedal

    return True


def harvest_and_measure():
    highest_pedal = 15
    while highest_pedal == 15:
        harvest()
        if num_items(Items.Power) < get_min(Items.Power):
            plant(Entities.Sunflower)
        while get_entity_type() == Entities.Sunflower and not can_harvest():
            water_tile()
            if buy(Items.Fertilizer, 100):
                use_item(Items.Fertilizer)
        highest_pedal = measure()
    if highest_pedal == None:
        return 0
    return highest_pedal
