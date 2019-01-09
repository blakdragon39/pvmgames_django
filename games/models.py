# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


'''
- competition
- game card
    - different games
- drops
    - bosses
    - items
    - combinations
'''


class Boss(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    image = models.CharField(max_length=100, null=False, blank=False)


class Item(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    image = models.CharField(max_length=100, null=False, blank=False)


class Drop(models.Model):
    boss = models.ForeignKey(Boss, null=True)
    # boss or an item or both
    # rarity
    pass
