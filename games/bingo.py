import random

from games.models import Drop, BingoCard, Item, Boss


def new_bingo_card(user, items, bosses, wilderness_bosses, slayer_bosses, slayer_level, free_space):
    drops = Drop.objects.all()

    if not wilderness_bosses:
        drops = drops.filter(boss__wilderness=False)

    if not slayer_bosses:
        drops = drops.filter(boss__slayer_level=0)

    drops = drops.filter(boss__slayer_level__lte=slayer_level)

    for drop in drops:
        print drop
