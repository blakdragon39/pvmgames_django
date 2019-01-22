# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from games.bingo import new_bingo_card
from games.forms import CompetitionForm, BingoForm
from games.models import BingoCard


# register = template.Library()
# @register.filter()
# def range(min=5):
#     return range(min)


@login_required
def new_competition(request):
    if request.method == 'POST':
        competition_form = CompetitionForm(request.POST)
        bingo_form = BingoForm(request.POST)
    else:
        competition_form = CompetitionForm()
        bingo_form = BingoForm()

    context = {
        'competition_form': competition_form,
        'bingo_form': bingo_form
    }

    return render(request, 'new_competition.html', context)


# @login_required
# def new_bingo_card(request, **kwargs):
#     if request.method == 'POST':
#         form = NewCardForm(request.POST)
#         if form.is_valid():
#             entity_choice = form.cleaned_data.get('entity_choice')
#             items = entity_choice == 'ITEMS' or entity_choice == 'BOTH'
#             bosses = entity_choice == 'BOSSES' or entity_choice == 'BOTH'
#             wilderness = form.cleaned_data.get('wilderness')
#             slayer = form.cleaned_data.get('slayer')
#             slayer_level = form.cleaned_data.get('slayer_level')
#             free_space = form.cleaned_data.get('free_space')
#
#             card = new_bingo_card(user=request.user,
#                                   items=items,
#                                   bosses=bosses,
#                                   wilderness_bosses=wilderness,
#                                   slayer_bosses=slayer,
#                                   slayer_level=slayer_level,
#                                   free_space=free_space)
#
#             return redirect('bingo-card', id=card.id)
#     else:
#         form = NewCardForm()
#
#     return render(request, 'new_card.html', {'form': form})


def bingo_card(request, **kwargs):
    card = BingoCard.objects.get(id=kwargs['id'])
    context = {'square_list': card.to_list()}
    return render(request, 'bingo_card.html', context)
