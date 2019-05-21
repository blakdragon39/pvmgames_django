from django import forms

from games.models import LeaderBoardCompetition


class CompetitionForm(forms.Form):
    game_choices = [
        ('LEADERBOARD', 'Leaderboard'),
        ('BINGO', 'Bingo')
    ]

    game_type = forms.ChoiceField(choices=game_choices)
    title = forms.CharField(max_length=200, required=True)


class BingoForm(forms.Form):
    entity_choices = [
        ('BOTH', 'Items and Bosses'),
        ('ITEMS', 'Items Only'),
        ('BOSSES', 'Bosses Only')
    ]

    entity_choice = forms.ChoiceField(widget=forms.RadioSelect, choices=entity_choices, initial='BOTH')
    wilderness = forms.BooleanField(initial=True, required=False)
    slayer = forms.BooleanField(initial=True, required=False)
    free_space = forms.BooleanField(initial=True, required=False)


class NewBingoCardForm(forms.Form):
    user_name = forms.CharField()
    slayer_level = forms.IntegerField(min_value=1, max_value=99, initial=99)


class LeaderBoardForm(forms.Form):
    alchemical_hydra = forms.BooleanField(required=False)
    abyssal_sire = forms.BooleanField(required=False)
    cerberus = forms.BooleanField(required=False)
    grotesque_guardians = forms.BooleanField(required=False)
    kraken = forms.BooleanField(required=False)
    thermonuclear_smoke_devil = forms.BooleanField(required=False)
    
    callisto = forms.BooleanField(required=False)
    chaos_elemental = forms.BooleanField(required=False)
    scorpia = forms.BooleanField(required=False)
    venenatis = forms.BooleanField(required=False)
    vetion = forms.BooleanField(required=False)
    
    zilyana = forms.BooleanField(required=False)
    graardor = forms.BooleanField(required=False)
    kree_arra = forms.BooleanField(required=False)
    kril_tsutsaroth = forms.BooleanField(required=False)
    
    prime = forms.BooleanField(required=False)
    rex = forms.BooleanField(required=False)
    supreme = forms.BooleanField(required=False)
    
    kalphite_queen = forms.BooleanField(required=False)
    king_black_dragon = forms.BooleanField(required=False)
    vorkath = forms.BooleanField(required=False)
    zulrah = forms.BooleanField(required=False)
