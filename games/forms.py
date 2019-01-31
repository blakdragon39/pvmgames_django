from django import forms

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
    abyssal_sire = forms.BooleanField()
    cerberus = forms.BooleanField()
    grotesque_guardians = forms.BooleanField()
    kraken = forms.BooleanField()
    thermonuclear_smoke_devil = forms.BooleanField()

    callisto = forms.BooleanField()
    chaos_elemental = forms.BooleanField()
    scorpia = forms.BooleanField()
    venenatis = forms.BooleanField()
    vetion = forms.BooleanField()

    zilyana = forms.BooleanField()
    graardor = forms.BooleanField()
    kree_arra = forms.BooleanField()
    kril_tsutsaroth = forms.BooleanField()

    prime = forms.BooleanField()
    rex = forms.BooleanField()
    supreme = forms.BooleanField()

    kalphite_queen = forms.BooleanField()
    king_black_dragon = forms.BooleanField()
    vorkath = forms.BooleanField()
    zulrah = forms.BooleanField()
