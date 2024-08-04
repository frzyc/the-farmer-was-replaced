def get_min_hay():
    return 50000


def get_min_wood():
    return 5000


# include empty and full tanks
def get_min_tanks():
    return 10000


def get_min_carrots():
    return 40000


def get_min_pumpkins():
    return 40000


def get_min_power():
    return 100000


def get_min_gold():
    return 100000


def get_min_cactus():
    return 100000


def get_min_dict():
    return {
        Items.Hay: get_min_hay(),
        Items.Wood: get_min_wood(),
        Items.Carrot: get_min_carrots(),
        Items.Pumpkin: get_min_pumpkins(),
        Items.Power: get_min_power(),
        Items.Gold: get_min_gold(),
        Items.Cactus: get_min_cactus(),
    }


def get_min(item):
    return get_min_dict()[item]


def get_grid(element):
    size = get_world_size()
    grid = []
    for _ in range(size):
        ygrid = []
        for _ in range(size):
            ygrid.append(element)
        grid.append(ygrid)
    return grid


def buy(item, num):
    if num_items(item) > num:
        return True
    cost = get_cost(item)
    for it in cost:
        # if num_items(it) < (get_min(it) + num * cost[it]):
        if num_items(it) < (num * cost[it]):
            return False
    trade(item, num)
    return True
