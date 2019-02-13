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


class LeaderBoardForm(forms.ModelForm):

    class Meta:
        model = LeaderBoardCompetition
        exclude = ['title', 'user']
