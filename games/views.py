# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from games.bingo import new_bingo_card
from games.forms import CompetitionForm, BingoForm, NewBingoCardForm
from games.models import BingoCard, Competition, BingoCompetition


@login_required
def new_competition(request):
    if request.method == 'POST':
        competition_form = CompetitionForm(request.POST)
        bingo_form = BingoForm(request.POST)

        if competition_form.is_valid():
            game_type = competition_form.cleaned_data.get('game_type')
            title = competition_form.cleaned_data.get('title')
            if game_type == 'BINGO' and bingo_form.is_valid():
                competition = create_bingo_competition(request.user, title, bingo_form)
                return redirect('competition', id=competition.id)

    else:
        competition_form = CompetitionForm()
        bingo_form = BingoForm()

    context = {
        'competition_form': competition_form,
        'bingo_form': bingo_form
    }

    return render(request, 'new_competition.html', context)


def competition_view(request, **kwargs):
    competition = Competition.objects.get(id=kwargs['id'])
    return render(request, 'competition.html', {'competition': competition})


def create_bingo_competition(user, title, form):
    entity_choice = form.cleaned_data.get('entity_choice')
    wilderness = form.cleaned_data.get('wilderness')
    slayer = form.cleaned_data.get('slayer')
    free_space = form.cleaned_data.get('free_space')

    return BingoCompetition.objects.create(user=user,
                                           title=title,
                                           type=entity_choice,
                                           wilderness=wilderness,
                                           slayer=slayer,
                                           free_space=free_space)


@login_required
def new_bingo_card_view(request, **kwargs):

    if request.method == 'POST':
        form = NewBingoCardForm(request.POST)
        competition = Competition.objects.get(id=kwargs['competition_id'])

        if request.user != competition.user:
            form.add_error(None, 'You are not the owner of this competition')
        elif form.is_valid():
            user_name = form.cleaned_data.get('user_name')
            slayer_level = form.cleaned_data.get('slayer_level')

            card = new_bingo_card(competition, user_name, slayer_level)

            return redirect('bingo-card', id=card.id)
    else:
        form = NewBingoCardForm()

    return render(request, 'new_card.html', {'form': form})


def bingo_card(request, **kwargs):
    card = BingoCard.objects.get(id=kwargs['id'])
    context = {'square_list': card.to_list()}
    return render(request, 'bingo_card.html', context)
