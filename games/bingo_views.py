from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from rest_framework import status

from games.bingo import create_new_bingo_card
from games.forms import NewBingoCardForm
from games.models import BingoCompetition, BingoCard, GameCard


def get_competition(competition_id):
    try:
        return BingoCompetition.objects.get(id=competition_id)
    except BingoCompetition.DoesNotExist:
        raise Http404


def get_competition_card(competition, card_id):
    try:
        return competition.game_cards.get(id=card_id)
    except GameCard.DoesNotExist:
        raise Http404


def get_card(card_id):
    try:
        return BingoCard.objects.get(id=card_id)
    except BingoCard.DoesNotExist:
        raise Http404


def bingo_competition_view(request, **kwargs):
    competition = get_competition(kwargs['id'])
    card_id = kwargs['card_id'] if 'card_id' in kwargs else request.GET.get('card_id')

    if card_id:
        card = get_competition_card(competition, card_id)
    else:
        card = competition.game_cards.first()

    context = {
        'competition': competition,
        'card': card
    }

    return render(request, 'bingo_competition.html', context)


@login_required
def new_bingo_card_view(request, **kwargs):
    if request.method == 'POST':
        form = NewBingoCardForm(request.POST)
        competition = get_competition(kwargs['competition_id'])

        if request.user != competition.user:
            form.add_error(None, 'You are not the owner of this competition')
        elif form.is_valid():
            user_name = form.cleaned_data.get('user_name')
            slayer_level = form.cleaned_data.get('slayer_level')

            card = create_new_bingo_card(competition, user_name, slayer_level)

            return redirect('bingo-competition', id=competition.id, card_id=card.id)
    else:
        form = NewBingoCardForm()

    return render(request, 'new_card.html', {'form': form})


def ajax_update_bingo_card(request):
    card_id = request.GET.get('card_id')
    square_id = int(request.GET.get('square_id')) + 1
    proof = request.GET.get('proof')

    card = get_card(card_id)

    if request.user != card.competition.user:
        return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)
    else:
        card.__setattr__('square' + str(square_id) + '_proof', proof)
        card.save()

        return HttpResponse()
