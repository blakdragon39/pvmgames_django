# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from games.models import *

admin.site.register(Item)
admin.site.register(Boss)
admin.site.register(Drop)
admin.site.register(BingoCard)
admin.site.register(BingoCompetition)
admin.site.register(LeaderBoardCompetition)
