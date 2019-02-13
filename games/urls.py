from django.conf.urls import url

from games.views import *

game_urls = [
    url(r'^new-competition/$', new_competition, name='new-competition'),
    url(r'^bingo/(?P<id>\d+)/$', bingo_competition_view, name='bingo-competition'),
    url(r'^leader-board/(?P<id>\d+)/$', leader_board_competition_view, name='leader-board-competition'),
    url(r'^bingo/(?P<competition_id>\d+)/new-bingo-card/$', new_bingo_card_view, name='new-bingo-card'),

    url(r'^ajax/update-bingo-card/$', ajax_update_bingo_card, name='update-bingo-card')
]
