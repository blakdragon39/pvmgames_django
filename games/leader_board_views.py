import json

from django.http import HttpResponse, Http404
from django.shortcuts import render
from rest_framework import status

from games.models import LeaderBoardCompetition, Drop, LeaderBoardCard, LeaderBoardDrop, LeaderBoardRank


def get_competition(competition_id):
    try:
        return LeaderBoardCompetition.objects.get(id=competition_id)
    except LeaderBoardCompetition.DoesNotExist:
        raise Http404


def get_leader_board_drop(competition, drop_id):
    try:
        if competition:
            return competition.drops.get(id=drop_id)
        else:
            return LeaderBoardDrop.objects.get(id=drop_id)
    except LeaderBoardDrop.DoesNotExist:
        raise Http404


def get_drop(drop_id):
    try:
        return Drop.objects.get(id=drop_id)
    except Drop.DoesNotExist:
        raise Http404


def leader_board_competition_view(request, **kwargs):
    competition = get_competition(kwargs['id'])
    drops = competition.drops.all()

    ranks_dict = {}

    for card in competition.game_cards.all():
        try:
            rank = ranks_dict[card.user_name]
        except KeyError:
            rank = LeaderBoardRank()
            ranks_dict[card.user_name] = rank

        rank.points += card.points  # Add total points
        rank.bonus_points += 1  # Add points for number of drops received
        rank.order = card.id * -1  # Getting a card first is worth more. higher id = lower sort order

    rankings = []

    for rank in ranks_dict:
        rankings.append((rank, ranks_dict[rank]))

    rankings.sort(key=lambda r: (r[1].points, r[1].bonus_points, r[1].order), reverse=True)

    context = {
        'competition': competition,
        'drops': drops,
        'rankings': rankings,
        'cards': competition.game_cards.order_by('id').all(),
        'names': competition.game_cards.values_list('user_name', flat=True).distinct().all()
    }

    return render(request, 'leader_board_competition.html', context)


def leader_board_configure_view(request, **kwargs):
    competition = get_competition(kwargs['id'])
    drops = LeaderBoardDrop.objects.filter(competition=competition)

    context = {
        'competition': competition,
        'drops': drops
    }

    return render(request, 'leader_board_configure.html', context)


def ajax_update_leader_board(request, **kwargs):
    competition_id = request.GET.get('competition_id')
    drop_id = request.GET.get('drop_id')
    username = request.GET.get('username')
    proof = request.GET.get('proof')

    competition = get_competition(competition_id)
    leader_board_drop = get_leader_board_drop(competition, drop_id)
    drop = get_drop(leader_board_drop.drop.id)

    if request.user != competition.user:
        return HttpResponse(status=status.HTTP_401_UNAUTHORIZED, content='You are not allowed to edit this competition')
    elif not competition.configured:
        return HttpResponse(status=status.HTTP_401_UNAUTHORIZED, content='You are not allowed to edit this competition')
    else:
        LeaderBoardCard.objects.create(competition=competition,
                                       user_name=username,
                                       proof=proof,
                                       drop=drop,
                                       points=leader_board_drop.points)
        return HttpResponse()


def ajax_configure_leader_board(request, **kwargs):
    values = json.loads(request.GET.get('values'))
    competition_id = request.GET.get('competition_id')

    for drop_id in values:
        drop = get_leader_board_drop(None, drop_id)

        if drop.competition.user != request.user:
            return HttpResponse(status=status.HTTP_401_UNAUTHORIZED,
                                content='You are not allowed to edit this competition')

        drop.points = values[drop_id]

        try:
            drop.save()
        except ValueError:
            return HttpResponse(status=status.HTTP_403_FORBIDDEN, content='One of the entered values is invalid')

    competition = get_competition(competition_id)
    competition.configured = True
    competition.save()

    return HttpResponse()
