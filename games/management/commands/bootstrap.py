import json

from django.core.management import BaseCommand

from games.models import Boss, Item, Drop


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('static/drops.json') as file_data:
            json_data = json.load(file_data)

            for json_item in json_data:
                boss_name, boss_file = json_item['boss'], json_item['boss_file']
                item_name, item_file = json_item['name'], json_item['item_file']

                item = add_item(item_name, item_file)
                boss = add_boss(boss_name, boss_file)
                print 'Adding ' + str(item) + ' - ' + str(boss)
                Drop.objects.create(main=item, sub=boss)


def add_item(name, image):
    try:
        item = Item.objects.get(name=name)
    except:
        item = Item.objects.create(name=name, image=image)

    return item


def add_boss(name, image):
    try:
        boss = Boss.objects.get(name=name)
    except:
        boss = Boss.objects.create(name=name, image=image)

    return boss
