# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from games.bingo import new_bingo_card
from games.forms import NewCardForm
from games.models import BingoCard


@login_required
def new_card(request, **kwargs):
    if request.method == 'POST':
        form = NewCardForm(request.POST)
        if form.is_valid():
            entity_choice = form.cleaned_data.get('entity_choice')
            print entity_choice
            # items = request.GET.get('items', False)
            # bosses = request.GET.get('bosses', False)
            # wilderness = request.GET.get('wilderness', True)
            # slayer = request.GET.get('slayer', True)
            # slayer_level = request.GET.get('slayer_level', 99)
            # free_space = request.GET.get('free_space', True)
            #
            # card = new_bingo_card(user=request.user,
            #                       items=items,
            #                       bosses=bosses,
            #                       wilderness_bosses=wilderness,
            #                       slayer_bosses=slayer,
            #                       slayer_level=slayer_level,
            #                       free_space=free_space)
            #
            # return redirect('bingo-card', id=card.id)
    else:
        form = NewCardForm()

    return render(request, 'new_card.html', {'form': form})


def bingo_card(request, **kwargs):
    card = BingoCard.objects.get(id=kwargs['id'])
    context = {'card': card}
    return render(request, 'bingo_card.html', context)
