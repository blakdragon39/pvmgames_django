from django.conf.urls import url

from games.views import new_bingo_card, bingo_card, new_competition

game_urls = [
    url(r'^new-competition/$', new_competition, name='new-competition'),
    url(r'^new-bingo-card/$', new_bingo_card, name='new-bingo-card'),
    url(r'^card/(?P<id>\d+)$', bingo_card, name='bingo-card')
]
