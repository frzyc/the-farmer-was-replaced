from solve_maze import *
from globals import *


def maze():
    if not buy(Items.Fertilizer, 100) or num_items(Items.Gold) > get_min(Items.Gold):
        return False
    clear()
    while True:
        plant(Entities.Bush)
        do_a_flip()
        if not buy(Items.Fertilizer, 100):
            break
        while num_items(Items.Fertilizer):
            use_item(Items.Fertilizer)
            if get_entity_type() == Entities.Hedge:
                break
        if get_entity_type() == Entities.Hedge:
            solve_maze()
