# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from polymorphic.models import PolymorphicModel


class RunescapeEntity(PolymorphicModel):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    _image = models.CharField(max_length=100, null=False, blank=False)

    def __unicode__(self):
        return self.name


class Boss(RunescapeEntity):
    wilderness = models.BooleanField(null=False)
    slayer = models.BooleanField(null=False)
    slayer_level = models.IntegerField()

    def get_image(self):
        return 'bosses/' + self._image

    def set_image(self, image):
        self._image = image

    image = property(get_image, set_image)


class Item(RunescapeEntity):
    def get_image(self):
        return 'items/' + self._image

    def set_image(self, image):
        self._image = image

    image = property(get_image, set_image)


class Drop(models.Model):
    item = models.ForeignKey(Item, null=False, on_delete=models.CASCADE)
    boss = models.ForeignKey(Boss, null=False, on_delete=models.CASCADE)
    drop_rate = models.IntegerField(null=False)

    def __unicode__(self):
        if self.item and self.boss:
            return str(self.boss) + ' - ' + str(self.item)
        elif self.item:
            return str(self.item)
        elif self.boss:
            return str(self.boss)


class Competition(PolymorphicModel):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=False, blank=False)

    def __unicode__(self):
        return self.title

    def get_type(self):
        return None


class GameCard(PolymorphicModel):
    competition = models.ForeignKey(Competition, null=False, on_delete=models.CASCADE, related_name='game_cards')
    user_name = models.CharField(max_length=50, null=False, blank=False)

    def __unicode__(self):
        return str(self.competition) + ' - ' + self.user_name


class LeaderBoardCompetition(Competition):
    configured = models.BooleanField(null=False, default=False)

    def get_type(self):
        return 'leader-board'


class LeaderBoardDrop(models.Model):
    competition = models.ForeignKey(LeaderBoardCompetition, null=False, on_delete=models.CASCADE, related_name='drops')
    drop = models.ForeignKey(Drop, null=False, on_delete=models.CASCADE)
    points = models.IntegerField(null=False, default=1)

    def __unicode__(self):
        return str(self.competition) + ' - ' + str(self.drop)


class LeaderBoardCard(GameCard):
    drop = models.ForeignKey(Drop, on_delete=models.CASCADE)
    proof = models.CharField(max_length=256)
    points = models.IntegerField(null=False, default=1)


class LeaderBoardRanking:
    def __init__(self, username, points):
        self.username = username
        self.points = points  # todo


class BingoCompetition(Competition):
    BINGO_TYPES = [
        ('ITEMS', 'Items'),
        ('BOSSES', 'Bosses'),
        ('BOTH', 'Items and Bosses')
    ]
    type = models.CharField(max_length=100, choices=BINGO_TYPES, null=False, blank=False)
    wilderness = models.BooleanField(null=False)
    slayer = models.BooleanField(null=False)
    free_space = models.BooleanField(null=False)

    def get_type(self):
        return 'bingo'


class BingoCard(GameCard):
    square1_main = models.ForeignKey(RunescapeEntity, null=False, on_delete=models.CASCADE, related_name='+')
    square1_sub = models.ForeignKey(RunescapeEntity, null=True, on_delete=models.CASCADE, related_name='+')
    square1_proof = models.CharField(max_length=500, null=True)

    square2_main = models.ForeignKey(RunescapeEntity, null=False, on_delete=models.CASCADE, related_name='+')
    square2_sub = models.ForeignKey(RunescapeEntity, null=True, on_delete=models.CASCADE, related_name='+')
    square2_proof = models.CharField(max_length=500, null=True)

    square3_main = models.ForeignKey(RunescapeEntity, null=False, on_delete=models.CASCADE, related_name='+')
    square3_sub = models.ForeignKey(RunescapeEntity, null=True, on_delete=models.CASCADE, related_name='+')
    square3_proof = models.CharField(max_length=500, null=True)

    square4_main = models.ForeignKey(RunescapeEntity, null=False, on_delete=models.CASCADE, related_name='+')
    square4_sub = models.ForeignKey(RunescapeEntity, null=True, on_delete=models.CASCADE, related_name='+')
    square4_proof = models.CharField(max_length=500, null=True)

    square5_main = models.ForeignKey(RunescapeEntity, null=False, on_delete=models.CASCADE, related_name='+')
    square5_sub = models.ForeignKey(RunescapeEntity, null=True, on_delete=models.CASCADE, related_name='+')
    square5_proof = models.CharField(max_length=500, null=True)

    square6_main = models.ForeignKey(RunescapeEntity, null=False, on_delete=models.CASCADE, related_name='+')
    square6_sub = models.ForeignKey(RunescapeEntity, null=True, on_delete=models.CASCADE, related_name='+')
    square6_proof = models.CharField(max_length=500, null=True)

    square7_main = models.ForeignKey(RunescapeEntity, null=False, on_delete=models.CASCADE, related_name='+')
    square7_sub = models.ForeignKey(RunescapeEntity, null=True, on_delete=models.CASCADE, related_name='+')
    square7_proof = models.CharField(max_length=500, null=True)

    square8_main = models.ForeignKey(RunescapeEntity, null=False, on_delete=models.CASCADE, related_name='+')
    square8_sub = models.ForeignKey(RunescapeEntity, null=True, on_delete=models.CASCADE, related_name='+')
    square8_proof = models.CharField(max_length=500, null=True)

    square9_main = models.ForeignKey(RunescapeEntity, null=False, on_delete=models.CASCADE, related_name='+')
    square9_sub = models.ForeignKey(RunescapeEntity, null=True, on_delete=models.CASCADE, related_name='+')
    square9_proof = models.CharField(max_length=500, null=True)

    square10_main = models.ForeignKey(RunescapeEntity, null=False, on_delete=models.CASCADE, related_name='+')
    square10_sub = models.ForeignKey(RunescapeEntity, null=True, on_delete=models.CASCADE, related_name='+')
    square10_proof = models.CharField(max_length=500, null=True)

    square11_main = models.ForeignKey(RunescapeEntity, null=False, on_delete=models.CASCADE, related_name='+')
    square11_sub = models.ForeignKey(RunescapeEntity, null=True, on_delete=models.CASCADE, related_name='+')
    square11_proof = models.CharField(max_length=500, null=True)

    square12_main = models.ForeignKey(RunescapeEntity, null=False, on_delete=models.CASCADE, related_name='+')
    square12_sub = models.ForeignKey(RunescapeEntity, null=True, on_delete=models.CASCADE, related_name='+')
    square12_proof = models.CharField(max_length=500, null=True)

    square13_main = models.ForeignKey(RunescapeEntity, null=True, on_delete=models.CASCADE, related_name='+')
    square13_sub = models.ForeignKey(RunescapeEntity, null=True, on_delete=models.CASCADE, related_name='+')
    square13_proof = models.CharField(max_length=500, null=True)

    square14_main = models.ForeignKey(RunescapeEntity, null=False, on_delete=models.CASCADE, related_name='+')
    square14_sub = models.ForeignKey(RunescapeEntity, null=True, on_delete=models.CASCADE, related_name='+')
    square14_proof = models.CharField(max_length=500, null=True)

    square15_main = models.ForeignKey(RunescapeEntity, null=False, on_delete=models.CASCADE, related_name='+')
    square15_sub = models.ForeignKey(RunescapeEntity, null=True, on_delete=models.CASCADE, related_name='+')
    square15_proof = models.CharField(max_length=500, null=True)

    square16_main = models.ForeignKey(RunescapeEntity, null=False, on_delete=models.CASCADE, related_name='+')
    square16_sub = models.ForeignKey(RunescapeEntity, null=True, on_delete=models.CASCADE, related_name='+')
    square16_proof = models.CharField(max_length=500, null=True)

    square17_main = models.ForeignKey(RunescapeEntity, null=False, on_delete=models.CASCADE, related_name='+')
    square17_sub = models.ForeignKey(RunescapeEntity, null=True, on_delete=models.CASCADE, related_name='+')
    square17_proof = models.CharField(max_length=500, null=True)

    square18_main = models.ForeignKey(RunescapeEntity, null=False, on_delete=models.CASCADE, related_name='+')
    square18_sub = models.ForeignKey(RunescapeEntity, null=True, on_delete=models.CASCADE, related_name='+')
    square18_proof = models.CharField(max_length=500, null=True)

    square19_main = models.ForeignKey(RunescapeEntity, null=False, on_delete=models.CASCADE, related_name='+')
    square19_sub = models.ForeignKey(RunescapeEntity, null=True, on_delete=models.CASCADE, related_name='+')
    square19_proof = models.CharField(max_length=500, null=True)

    square20_main = models.ForeignKey(RunescapeEntity, null=False, on_delete=models.CASCADE, related_name='+')
    square20_sub = models.ForeignKey(RunescapeEntity, null=True, on_delete=models.CASCADE, related_name='+')
    square20_proof = models.CharField(max_length=500, null=True)

    square21_main = models.ForeignKey(RunescapeEntity, null=False, on_delete=models.CASCADE, related_name='+')
    square21_sub = models.ForeignKey(RunescapeEntity, null=True, on_delete=models.CASCADE, related_name='+')
    square21_proof = models.CharField(max_length=500, null=True)

    square22_main = models.ForeignKey(RunescapeEntity, null=False, on_delete=models.CASCADE, related_name='+')
    square22_sub = models.ForeignKey(RunescapeEntity, null=True, on_delete=models.CASCADE, related_name='+')
    square22_proof = models.CharField(max_length=500, null=True)

    square23_main = models.ForeignKey(RunescapeEntity, null=False, on_delete=models.CASCADE, related_name='+')
    square23_sub = models.ForeignKey(RunescapeEntity, null=True, on_delete=models.CASCADE, related_name='+')
    square23_proof = models.CharField(max_length=500, null=True)

    square24_main = models.ForeignKey(RunescapeEntity, null=False, on_delete=models.CASCADE, related_name='+')
    square24_sub = models.ForeignKey(RunescapeEntity, null=True, on_delete=models.CASCADE, related_name='+')
    square24_proof = models.CharField(max_length=500, null=True)

    square25_main = models.ForeignKey(RunescapeEntity, null=False, on_delete=models.CASCADE, related_name='+')
    square25_sub = models.ForeignKey(RunescapeEntity, null=True, on_delete=models.CASCADE, related_name='+')
    square25_proof = models.CharField(max_length=500, null=True)

    def to_list(self):
        return [(self.square1_main, self.square1_sub, self.square1_proof),
                (self.square2_main, self.square2_sub, self.square2_proof),
                (self.square3_main, self.square3_sub, self.square3_proof),
                (self.square4_main, self.square4_sub, self.square4_proof),
                (self.square5_main, self.square5_sub, self.square5_proof),
                (self.square6_main, self.square6_sub, self.square6_proof),
                (self.square7_main, self.square7_sub, self.square7_proof),
                (self.square8_main, self.square8_sub, self.square8_proof),
                (self.square9_main, self.square9_sub, self.square9_proof),
                (self.square10_main, self.square10_sub, self.square10_proof),
                (self.square11_main, self.square11_sub, self.square11_proof),
                (self.square12_main, self.square12_sub, self.square12_proof),
                (self.square13_main, self.square13_sub, self.square13_proof),
                (self.square14_main, self.square14_sub, self.square14_proof),
                (self.square15_main, self.square15_sub, self.square15_proof),
                (self.square16_main, self.square16_sub, self.square16_proof),
                (self.square17_main, self.square17_sub, self.square17_proof),
                (self.square18_main, self.square18_sub, self.square18_proof),
                (self.square19_main, self.square19_sub, self.square19_proof),
                (self.square20_main, self.square20_sub, self.square20_proof),
                (self.square21_main, self.square21_sub, self.square21_proof),
                (self.square22_main, self.square22_sub, self.square22_proof),
                (self.square23_main, self.square23_sub, self.square23_proof),
                (self.square24_main, self.square24_sub, self.square24_proof),
                (self.square25_main, self.square25_sub, self.square25_proof)]
