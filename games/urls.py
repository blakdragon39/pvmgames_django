from django.conf.urls import url

from games.views import new_bingo_card_view, new_competition, bingo_competition_view, ajax_get_bingo_card

game_urls = [
    url(r'^new-competition/$', new_competition, name='new-competition'),
    url(r'^bingo/(?P<id>\d+)/$', bingo_competition_view, name='bingo-competition'),
    url(r'^bingo/(?P<competition_id>\d+)/new-bingo-card/$', new_bingo_card_view, name='new-bingo-card'),

    url(r'^ajax/bingo/$', ajax_get_bingo_card, name='reload-bingo'),
]
