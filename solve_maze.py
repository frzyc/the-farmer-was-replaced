# always keep a wall to the right-hand size
def solve_maze():
    last_dir = East
    while get_entity_type() != Entities.Treasure:
        dir_to_try = []
        if last_dir == East:
            dir_to_try = [South, East, North, West]
        elif last_dir == South:
            dir_to_try = [West, South, East, North]
        elif last_dir == West:
            dir_to_try = [North, West, South, East]
        elif last_dir == North:
            dir_to_try = [East, North, West, South]
        for dir in dir_to_try:
            if move_maze(dir):
                last_dir = dir
                break 
    harvest()
