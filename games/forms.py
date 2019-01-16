from django import forms


class NewCardForm(forms.Form):
    entity_choices = [
        ('BOTH', 'Items and Bosses'),
        ('ITEMS', 'Items Only'),
        ('BOSSES', 'Bosses Only')
    ]

    entity_choice = forms.ChoiceField(widget=forms.RadioSelect, choices=entity_choices, initial='BOTH')
    wilderness = forms.BooleanField(initial=True, required=False)
    slayer = forms.BooleanField(initial=True, required=False)
    slayer_level = forms.IntegerField(min_value=0, max_value=99, initial=99)
    free_space = forms.BooleanField(initial=True, required=False)
