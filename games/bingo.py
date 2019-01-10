import random

from games.models import Drop


def new_bingo_card():
    drops = list(Drop.objects.all())
    card_drops = []

    for i in range(25):
        length = len(drops) - 1
        drop_i = random.randint(1, length)
        drop = drops.pop(drop_i)
        card_drops.append(drop)

    return card_drops
