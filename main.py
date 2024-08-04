from move_drone import *
from handle_grass_tree import *
from plant_pumpkin import *
from globals import *
from sunflower_list import *
from polyculture import *
from maze import *
from cactus import *
from dinosaur import *


def main():
    while True:
        dinosaur()
        cactus()
        maze()
        sunflower_list()
        plant_pumpkin()
        polyculture()


clear()
main()
