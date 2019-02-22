from django.conf.urls import url

from games.bingo_views import bingo_competition_view, new_bingo_card_view, ajax_update_bingo_card
from games.leader_board_views import leader_board_competition_view, ajax_update_leader_board, \
    leader_board_configure_view, ajax_configure_leader_board
from games.views import *

game_urls = [
    url(r'^new-competition/$', new_competition, name='new-competition'),

    url(r'^bingo/(?P<id>\d+)/$', bingo_competition_view, name='bingo-competition'),
    url(r'^bingo/(?P<competition_id>\d+)/new-bingo-card/$', new_bingo_card_view, name='new-bingo-card'),
    url(r'^ajax/update-bingo-card/$', ajax_update_bingo_card, name='update-bingo-card'),

    url(r'^leader-board/(?P<id>\d+)/$', leader_board_competition_view, name='leader-board-competition'),
    url(r'^leader-board/(?P<id>\d+)/configure/$', leader_board_configure_view, name='leader-board-configure'),
    url(r'^ajax/update-leader-board/$', ajax_update_leader_board, name='update-leader-board'),
    url(r'^ajax/configure-leader-board/$', ajax_configure_leader_board, name='configure-leader-board')
]
