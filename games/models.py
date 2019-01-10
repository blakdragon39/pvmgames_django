# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


'''
- competition: can have multiple people and is managed by one person
- game card: 
    - different games
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


class GameCard(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)


class BingoCard(GameCard):
    square1 = models.ForeignKey(Drop, null=False, on_delete=models.CASCADE, related_name='+')
    square2 = models.ForeignKey(Drop, null=False, on_delete=models.CASCADE, related_name='+')
    square3 = models.ForeignKey(Drop, null=False, on_delete=models.CASCADE, related_name='+')
    square4 = models.ForeignKey(Drop, null=False, on_delete=models.CASCADE, related_name='+')
    square5 = models.ForeignKey(Drop, null=False, on_delete=models.CASCADE, related_name='+')
    square6 = models.ForeignKey(Drop, null=False, on_delete=models.CASCADE, related_name='+')
    square7 = models.ForeignKey(Drop, null=False, on_delete=models.CASCADE, related_name='+')
    square8 = models.ForeignKey(Drop, null=False, on_delete=models.CASCADE, related_name='+')
    square9 = models.ForeignKey(Drop, null=False, on_delete=models.CASCADE, related_name='+')
    square10 = models.ForeignKey(Drop, null=False, on_delete=models.CASCADE, related_name='+')
    square11 = models.ForeignKey(Drop, null=False, on_delete=models.CASCADE, related_name='+')
    square12 = models.ForeignKey(Drop, null=False, on_delete=models.CASCADE, related_name='+')
    square13 = models.ForeignKey(Drop, null=False, on_delete=models.CASCADE, related_name='+')
    square14 = models.ForeignKey(Drop, null=False, on_delete=models.CASCADE, related_name='+')
    square15 = models.ForeignKey(Drop, null=False, on_delete=models.CASCADE, related_name='+')
    square16 = models.ForeignKey(Drop, null=False, on_delete=models.CASCADE, related_name='+')
    square17 = models.ForeignKey(Drop, null=False, on_delete=models.CASCADE, related_name='+')
    square18 = models.ForeignKey(Drop, null=False, on_delete=models.CASCADE, related_name='+')
    square19 = models.ForeignKey(Drop, null=False, on_delete=models.CASCADE, related_name='+')
    square20 = models.ForeignKey(Drop, null=False, on_delete=models.CASCADE, related_name='+')
    square21 = models.ForeignKey(Drop, null=False, on_delete=models.CASCADE, related_name='+')
    square22 = models.ForeignKey(Drop, null=False, on_delete=models.CASCADE, related_name='+')
    square23 = models.ForeignKey(Drop, null=False, on_delete=models.CASCADE, related_name='+')
    square24 = models.ForeignKey(Drop, null=False, on_delete=models.CASCADE, related_name='+')
    square25 = models.ForeignKey(Drop, null=False, on_delete=models.CASCADE, related_name='+')
