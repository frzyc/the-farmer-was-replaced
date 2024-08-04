from globals import *
from plant_field import *
from move_drone import *


def dinosaur():
    size = get_world_size()
    buy_num = size * size * 10
    if not buy(Items.Egg, buy_num):
        return False
    clear()
    # use all
    while True:
        use_item(Items.Egg)
        move_drone()
        if get_pos_x() == 0 and get_pos_y() == 0:
            break
    dirs = [North, South, East, West]
    while True:
        if get_entity_type() != Entities.Dinosaur and num_items(Items.Egg):
            use_item(Items.Egg)
        x = get_pos_x()
        y = get_pos_y()
        if x == 0 and y == 0 and num_items(Items.Egg) == 0:
            return False
        current = measure()
        count = 1
        for d in dirs:
            if measure(d) == current:
                count += 1
        if count >= 4:
            harvest()
        move_drone()
