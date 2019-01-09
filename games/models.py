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
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    image = models.CharField(max_length=100, null=False, blank=False)

    def __unicode__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    image = models.CharField(max_length=100, null=False, blank=False)

    def __unicode__(self):
        return self.name


class Drop(models.Model):
    boss = models.ForeignKey(Boss, null=True, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, null=True, on_delete=models.CASCADE)

    def __unicode__(self):
        if self.boss and self.item:
            return str(self.item) + ' - ' + str(self.boss)
        elif self.item:
            return str(self.item)
        elif self.boss:
            return str(self.boss)
