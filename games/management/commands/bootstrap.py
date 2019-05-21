import json

from django.core.management import BaseCommand

from games.models import Boss, Item, Drop


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('bingo/static/initial_data.json') as file_data:
            json_data = json.load(file_data)
            boss_data = json_data['bosses']
            item_data = json_data['items']
            drop_data = json_data['drops']

            for json_boss in boss_data:
                update_boss(json_boss)

            for json_item in item_data:
                update_item(json_item)

            for json_drop in drop_data:
                update_drop(json_drop)


def update_boss(json_boss):
    print 'Adding or updating ' + json_boss['name']

    slayer_level = json_boss['slayer_level']
    defaults = {
        'image': json_boss['file'],
        'wilderness': json_boss['wilderness'],
        'slayer': slayer_level is not 0,
        'slayer_level': slayer_level
    }

    Boss.objects.update_or_create(name=json_boss['name'], defaults=defaults)


def update_item(json_item):
    print 'Adding or updating ' + json_item['name']

    defaults = {
        'image': json_item['file']
    }

    Item.objects.update_or_create(name=json_item['name'], defaults=defaults)


def update_drop(json_drop):
    item = Item.objects.get(name=json_drop['item'])
    boss = Boss.objects.get(name=json_drop['boss'])
    print 'Adding or updating ' + str(item) + ' for ' + str(boss)

    defaults = {
        'drop_rate': json_drop['drop_rate']
    }

    Drop.objects.update_or_create(item=item, boss=boss, defaults=defaults)
