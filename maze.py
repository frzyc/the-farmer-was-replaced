from solve_maze import *

clear()
while True:
    plant(Entities.Bush)
    do_a_flip()
    if num_items(Items.Fertilizer) < 100:
        trade(Items.Fertilizer, 100)
    for i in range(100):
        use_item(Items.Fertilizer)
        if get_entity_type() == Entities.Hedge:
            break
    if get_entity_type() == Entities.Hedge:
        solve_maze()
