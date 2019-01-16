from django.conf.urls import url

from games.views import new_card, bingo_card

game_urls = [
    url(r'^new-card/$', new_card, name='new-card'),
    url(r'^card/(?P<id>\d+)$', bingo_card, name='bingo-card')
]
