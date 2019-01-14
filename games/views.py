# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from games.bingo import new_bingo_card
from games.models import BingoCard


@login_required
def new_card(request):
    card_drops = new_bingo_card()
    card = BingoCard.objects.create(user=request.user,
                                    square1=card_drops[0],
                                    square2=card_drops[1],
                                    square3=card_drops[2],
                                    square4=card_drops[3],
                                    square5=card_drops[4],
                                    square6=card_drops[5],
                                    square7=card_drops[6],
                                    square8=card_drops[7],
                                    square9=card_drops[8],
                                    square10=card_drops[9],
                                    square11=card_drops[10],
                                    square12=card_drops[11],
                                    square13=card_drops[12],
                                    square14=card_drops[13],
                                    square15=card_drops[14],
                                    square16=card_drops[15],
                                    square17=card_drops[16],
                                    square18=card_drops[17],
                                    square19=card_drops[18],
                                    square20=card_drops[19],
                                    square21=card_drops[20],
                                    square22=card_drops[21],
                                    square23=card_drops[22],
                                    square24=card_drops[23],
                                    square25=card_drops[24])

    return redirect('bingo-card', id=card.id)


def bingo_card(request, **kwargs):
    card = BingoCard.objects.get(id=kwargs['id'])
    context = {'card': card}
    return render(request, 'bingo_card.html', context)
