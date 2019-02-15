from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status

from games.models import LeaderBoardCompetition, Drop, LeaderBoardCard, LeaderBoardBoss


def leader_board_competition_view(request, **kwargs):
    competition = LeaderBoardCompetition.objects.get(id=kwargs['id'])
    bosses = LeaderBoardBoss.objects.filter(competition=competition).values_list('boss')
    drops = Drop.objects.filter(boss__in=bosses)

    ranks_dict = {}
    rankings = []

    for card in competition.game_cards.all():
        try:
            ranks_dict[card.user_name] += 1  # todo pts
        except KeyError:
            ranks_dict[card.user_name] = 1  # todo pts

    for rank in ranks_dict:
        rankings.append((rank, ranks_dict[rank]))

    rankings.sort(key=lambda r: r[1], reverse=True)

    print rankings

    context = {
        'competition': competition,
        'drops': drops,
        'rankings': rankings
    }

    return render(request, 'leader_board_competition.html', context)


def ajax_update_leader_board(request, **kwargs):
    competition_id = request.GET.get('competition_id')
    drop_id = request.GET.get('drop_id')
    username = request.GET.get('username')
    proof = request.GET.get('proof')

    competition = LeaderBoardCompetition.objects.get(id=competition_id)
    drop = Drop.objects.get(id=drop_id)

    if request.user != competition.user:
        return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)
    else:
        LeaderBoardCard.objects.create(competition=competition,
                                       user_name=username,
                                       proof=proof,
                                       drop=drop)
        return HttpResponse()