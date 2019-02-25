import json

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status

from games.models import LeaderBoardCompetition, Drop, LeaderBoardCard, LeaderBoardDrop, LeaderBoardRank


def leader_board_competition_view(request, **kwargs):
    competition = LeaderBoardCompetition.objects.get(id=kwargs['id'])
    drops = competition.drops.all()

    ranks_dict = {}

    for card in competition.game_cards.all():
        try:
            rank = ranks_dict[card.user_name]
        except KeyError:
            rank = LeaderBoardRank()
            ranks_dict[card.user_name] = rank

        rank.points += card.points
        rank.bonus_points += 1

    rankings = []

    for rank in ranks_dict:
        rankings.append((rank, ranks_dict[rank]))

    rankings.sort(key=lambda r: (r[1].points, r[1].bonus_points), reverse=True)

    context = {
        'competition': competition,
        'drops': drops,
        'rankings': rankings
    }

    return render(request, 'leader_board_competition.html', context)


def leader_board_configure_view(request, **kwargs):
    competition = LeaderBoardCompetition.objects.get(id=kwargs['id'])
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

    competition = LeaderBoardCompetition.objects.get(id=competition_id)
    leader_board_drop = LeaderBoardDrop.objects.get(competition=competition, id=drop_id)
    drop = Drop.objects.get(id=leader_board_drop.drop.id)

    if request.user != competition.user:
        return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)  # todo error message?
    elif not competition.configured:
        return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)  # todo error message?
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
        drop = LeaderBoardDrop.objects.get(id=drop_id)

        if drop.competition.user != request.user:
            return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)  # todo error message?

        drop.points = values[drop_id]

        try:
            drop.save()
        except ValueError:
            return HttpResponse(status=status.HTTP_403_FORBIDDEN)  # todo error message

    competition = LeaderBoardCompetition.objects.get(id=competition_id)
    competition.configured = True
    competition.save()

    return HttpResponse()
