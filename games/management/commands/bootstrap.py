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
                Drop.objects.create(item=item, boss=boss)


def add_item(name, image):
    print 'Adding ' + name
    try:
        item = Item.objects.get(name=name)
        item.delete()
    except Item.DoesNotExist:
        pass

    item = Item.objects.create(name=name, image=image)
    return item


def add_boss(name, image):
    print 'Adding ' + name
    try:
        boss = Boss.objects.get(name=name)
        boss.delete()
    except Boss.DoesNotExist:
        pass

    boss = Boss.objects.create(name=name, image=image)
    return boss
