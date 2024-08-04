from move_drone import *
from handle_grass_tree import *
from plant_pumpkin import *
from globals import *
from plant_sunflowers import *


def main():
    planting_pumpkin = True
    while True:
        plant_sunflowers()
        if planting_pumpkin:
            if not plant_pumpkin():
                planting_pumpkin = False
                # TODO: need to renable pumpkin somhow?
        if not planting_pumpkin:
            handle_grass_tree()
        move_drone()


clear()
main()
