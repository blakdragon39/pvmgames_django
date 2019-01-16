import random

from games.models import Drop, BingoCard, Item, Boss


def new_bingo_card(user, items, bosses, wilderness_bosses, slayer_bosses, slayer_level, free_space):
    drops = Drop.objects.all()

    if not wilderness_bosses:
        drops = drops.filter(boss__wilderness=False)

    if not slayer_bosses:
        drops = drops.filter(boss__slayer_level=0)

    drops = drops.filter(boss__slayer_level__lte=slayer_level)

    if items and bosses:
        entities = drops
    elif items:
        entities = get_unique_items(drops)
    else:
        entities = get_bosses(drops)

    for entity in entities:
        print entity


def get_unique_items(drops):
    items = []
    for drop in drops:
        if drop.item not in items:
            items.append(drop.item)

    return items


def get_bosses(drops):
    bosses = []
    for drop in drops:
        bosses.append(drop.boss)

    return bosses
