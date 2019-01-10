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
                                    square1=card_drops[1],
                                    square2=card_drops[2],
                                    square3=card_drops[3],
                                    square4=card_drops[4],
                                    square5=card_drops[5],
                                    square6=card_drops[6],
                                    square7=card_drops[7],
                                    square8=card_drops[8],
                                    square9=card_drops[9],
                                    square10=card_drops[10],
                                    square11=card_drops[11],
                                    square12=card_drops[12],
                                    square13=card_drops[13],
                                    square14=card_drops[14],
                                    square15=card_drops[15],
                                    square16=card_drops[16],
                                    square17=card_drops[17],
                                    square18=card_drops[18],
                                    square19=card_drops[19],
                                    square20=card_drops[20],
                                    square21=card_drops[21],
                                    square22=card_drops[22],
                                    square23=card_drops[23],
                                    square24=card_drops[24],
                                    square25=card_drops[25])

    return redirect('bingo-card', id=card.id)


def bingo_card(request):
    return render(request, 'home.html')
