from django.conf.urls import url

from games.views import new_bingo_card_view, bingo_card, new_competition, competition_view

game_urls = [
    url(r'^new-competition/$', new_competition, name='new-competition'),
    url(r'^competition/(?P<id>\d+)/$', competition_view, name='competition'),
    url(r'^competition/(?P<competition_id>\d+)/new-bingo-card/$', new_bingo_card_view, name='new-bingo-card'),
    url(r'^card/(?P<id>\d+)/$', bingo_card, name='bingo-card')
]
