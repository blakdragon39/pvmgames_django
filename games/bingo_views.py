from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework import status

from games.bingo import create_new_bingo_card
from games.forms import NewBingoCardForm
from games.models import BingoCompetition, Competition, BingoCard


def bingo_competition_view(request, **kwargs):
    competition = BingoCompetition.objects.get(id=kwargs['id'])
    card_id = request.GET.get('card_id')  # todo DoesNotExist case (404)

    if card_id:
        card = competition.game_cards.get(id=card_id)
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
        competition = Competition.objects.get(id=kwargs['competition_id'])

        if request.user != competition.user:
            form.add_error(None, 'You are not the owner of this competition')
        elif form.is_valid():
            user_name = form.cleaned_data.get('user_name')
            slayer_level = form.cleaned_data.get('slayer_level')

            create_new_bingo_card(competition, user_name, slayer_level)

            return redirect('bingo-competition', id=competition.id)
    else:
        form = NewBingoCardForm()

    return render(request, 'new_card.html', {'form': form})


def ajax_update_bingo_card(request):
    card_id = request.GET.get('card_id')
    square_id = int(request.GET.get('square_id')) + 1
    proof = request.GET.get('proof')

    card = BingoCard.objects.get(id=card_id)

    if request.user != card.competition.user:
        return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)
    else:
        card.__setattr__('square' + str(square_id) + '_proof', proof)
        card.save()

        return HttpResponse()
