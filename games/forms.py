from django import forms


class CompetitionForm(forms.Form):
    game_choices = [
        ('BINGO', 'Bingo'),
        ('LEADERBOARD', 'Leaderboard')
    ]

    game_type = forms.ChoiceField(choices=game_choices)


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
