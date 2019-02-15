# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from games.forms import CompetitionForm, BingoForm, LeaderBoardForm
from games.models import BingoCompetition, LeaderBoardCompetition, LeaderBoardBoss, Boss


@login_required
def new_competition(request):
    if request.method == 'POST':
        competition_form = CompetitionForm(request.POST)
        bingo_form = BingoForm(request.POST)
        leader_board_form = LeaderBoardForm(request.POST)

        check_leader_board_errors(request, leader_board_form)

        if competition_form.is_valid():
            game_type = competition_form.cleaned_data.get('game_type')
            title = competition_form.cleaned_data.get('title')

            if game_type == 'BINGO' and bingo_form.is_valid():
                competition = create_bingo_competition(request.user, title, bingo_form)
                return redirect('bingo-competition', id=competition.id)
            elif game_type == 'LEADERBOARD' and leader_board_form.is_valid():
                competition = create_leader_board_competition(request.user, title, leader_board_form)
                return redirect('leader-board-competition', id=competition.id)

    else:
        competition_form = CompetitionForm()
        bingo_form = BingoForm()
        leader_board_form = LeaderBoardForm()

    context = {
        'competition_form': competition_form,
        'bingo_form': bingo_form,
        'leader_board_form': leader_board_form
    }

    return render(request, 'new_competition.html', context)


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


def check_leader_board_errors(request, form):
    error = True

    for field in form.fields:
        if request.POST.get(field):
            error = False

    if error:
        form.add_error(None, 'You must choose at least one boss to create a competition')


def create_leader_board_competition(user, title, form):
    competition = LeaderBoardCompetition.objects.create(user=user, title=title)

    if form.cleaned_data['abyssal_sire']:
        LeaderBoardBoss.objects.create(competition=competition, boss=Boss.objects.get(name='Abyssal Sire'))

    if form.cleaned_data['cerberus']:
        LeaderBoardBoss.objects.create(competition=competition, boss=Boss.objects.get(name='Cerberus'))

    if form.cleaned_data['grotesque_guardians']:
        LeaderBoardBoss.objects.create(competition=competition, boss=Boss.objects.get(name='Grotesque Guardians'))

    if form.cleaned_data['kraken']:
        LeaderBoardBoss.objects.create(competition=competition, boss=Boss.objects.get(name='Kraken'))

    if form.cleaned_data['thermonuclear_smoke_devil']:
        LeaderBoardBoss.objects.create(competition=competition, boss=Boss.objects.get(name='Thermonuclear Smoke Devil'))

    if form.cleaned_data['callisto']:
        LeaderBoardBoss.objects.create(competition=competition, boss=Boss.objects.get(name='Callisto'))

    if form.cleaned_data['chaos_elemental']:
        LeaderBoardBoss.objects.create(competition=competition, boss=Boss.objects.get(name='Chaos Elemental'))

    if form.cleaned_data['scorpia']:
        LeaderBoardBoss.objects.create(competition=competition, boss=Boss.objects.get(name='Scorpia'))

    if form.cleaned_data['venenatis']:
        LeaderBoardBoss.objects.create(competition=competition, boss=Boss.objects.get(name='Venenatis'))

    if form.cleaned_data['vetion']:
        LeaderBoardBoss.objects.create(competition=competition, boss=Boss.objects.get(name='Vet\'ion'))

    if form.cleaned_data['zilyana']:
        LeaderBoardBoss.objects.create(competition=competition, boss=Boss.objects.get(name='Commander Zilyana'))

    if form.cleaned_data['graardor']:
        LeaderBoardBoss.objects.create(competition=competition, boss=Boss.objects.get(name='General Graardor'))

    if form.cleaned_data['kree_arra']:
        LeaderBoardBoss.objects.create(competition=competition, boss=Boss.objects.get(name='Kree\'Arra'))

    if form.cleaned_data['kril_tsutsaroth']:
        LeaderBoardBoss.objects.create(competition=competition, boss=Boss.objects.get(name='Kril Tsutsaroth'))

    if form.cleaned_data['prime']:
        LeaderBoardBoss.objects.create(competition=competition, boss=Boss.objects.get(name='Dagannoth Prime'))

    if form.cleaned_data['rex']:
        LeaderBoardBoss.objects.create(competition=competition, boss=Boss.objects.get(name='Dagannoth Rex'))

    if form.cleaned_data['supreme']:
        LeaderBoardBoss.objects.create(competition=competition, boss=Boss.objects.get(name='Dagannoth Supreme'))

    if form.cleaned_data['kalphite_queen']:
        LeaderBoardBoss.objects.create(competition=competition, boss=Boss.objects.get(name='Kalphite Queen'))

    if form.cleaned_data['king_black_dragon']:
        LeaderBoardBoss.objects.create(competition=competition, boss=Boss.objects.get(name='King Black Dragon'))

    if form.cleaned_data['vorkath']:
        LeaderBoardBoss.objects.create(competition=competition, boss=Boss.objects.get(name='Vorkath'))

    if form.cleaned_data['zulrah']:
        LeaderBoardBoss.objects.create(competition=competition, boss=Boss.objects.get(name='Zulrah'))

    return competition
