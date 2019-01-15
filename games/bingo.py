import random

from games.models import Drop, BingoCard, Item, Boss


def new_bingo_card(user, items, bosses, wilderness_bosses, slayer_bosses, slayer_level, free_space):
    entities = []

    if items and bosses:
        entities = Drop.objects.all()
    elif items:
        entities = Item.objects.all()
    elif bosses:
        entities = Boss.objects.all()

    card = BingoCard.objects.create(user=user)  # todo all 25 spaces
    return card
