from django.conf.urls import url

from games.views import *

game_urls = [
    url(r'^new-competition/$', new_competition, name='new-competition'),
    url(r'^bingo/(?P<id>\d+)/$', bingo_competition_view, name='bingo-competition'),
    url(r'^bingo/(?P<competition_id>\d+)/new-bingo-card/$', new_bingo_card_view, name='new-bingo-card'),

    url(r'^ajax/get-bingo-card/$', ajax_get_bingo_card, name='get-bingo-card'),
    url(r'^ajax/get-bingo-square/$', ajax_get_bingo_square, name='get-bingo-square'),
    url(r'^ajax/update-bingo-card/$', ajax_update_bingo_card, name='update-bingo-card')
]
