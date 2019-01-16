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
        entities = list(drops)
    elif items:
        entities = get_unique_items(drops)
    else:
        entities = get_bosses(drops)

    card_items = []
    for i in range(25):
        if i == 13 and free_space:
            card_items.append(None)
        else:
            index = random.randint(0, len(entities) - 1)
            card_items.append(entities.pop(index))

    if items and bosses:
        return create_new_drops_card(user, card_items)
    else:
        return create_new_entity_card(user, card_items)


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


def create_new_drops_card(user, card_items):
    return BingoCard.objects.create(user=user,
                                    square1_main=card_items[0].item,
                                    square1_sub=card_items[0].boss,
                                    square2_main=card_items[1].item,
                                    square2_sub=card_items[1].boss,
                                    square3_main=card_items[2].item,
                                    square3_sub=card_items[2].boss,
                                    square4_main=card_items[3].item,
                                    square4_sub=card_items[3].boss,
                                    square5_main=card_items[4].item,
                                    square5_sub=card_items[4].boss,
                                    square6_main=card_items[5].item,
                                    square6_sub=card_items[5].boss,
                                    square7_main=card_items[6].item,
                                    square7_sub=card_items[6].boss,
                                    square8_main=card_items[7].item,
                                    square8_sub=card_items[7].boss,
                                    square9_main=card_items[8].item,
                                    square9_sub=card_items[8].boss,
                                    square10_main=card_items[9].item,
                                    square10_sub=card_items[9].boss,
                                    square11_main=card_items[10].item,
                                    square11_sub=card_items[10].boss,
                                    square12_main=card_items[11].item,
                                    square12_sub=card_items[11].boss,
                                    square13_main=card_items[12].item,
                                    square13_sub=card_items[12].boss,
                                    square14_main=card_items[13].item,
                                    square14_sub=card_items[13].boss,
                                    square15_main=card_items[14].item,
                                    square15_sub=card_items[14].boss,
                                    square16_main=card_items[15].item,
                                    square16_sub=card_items[15].boss,
                                    square17_main=card_items[16].item,
                                    square17_sub=card_items[16].boss,
                                    square18_main=card_items[17].item,
                                    square18_sub=card_items[17].boss,
                                    square19_main=card_items[18].item,
                                    square19_sub=card_items[18].boss,
                                    square20_main=card_items[19].item,
                                    square20_sub=card_items[19].boss,
                                    square21_main=card_items[20].item,
                                    square21_sub=card_items[20].boss,
                                    square22_main=card_items[21].item,
                                    square22_sub=card_items[21].boss,
                                    square23_main=card_items[22].item,
                                    square23_sub=card_items[22].boss,
                                    square24_main=card_items[23].item,
                                    square24_sub=card_items[23].boss,
                                    square25_main=card_items[24].item,
                                    square25_sub=card_items[24].boss)
