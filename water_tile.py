from globals import *


def water_tile():
    if get_ground_type() != Grounds.Soil:
        return
    # cannot use the #buy() function because of empty + full tanks
    tanks = num_items(Items.Empty_Tank) + num_items(Items.Water_Tank)
    if tanks < get_min_tanks() and num_items(Items.Wood) > (get_min_wood() + 5 * 100):
        trade(Items.Empty_Tank, 100)
    while get_water() < 0.75 and num_items(Items.Water_Tank) >= 1:
        use_item(Items.Water_Tank)
