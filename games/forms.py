from django import forms


class NewCardForm(forms.Form):
    entity_choices = [
        ('Items and Bosses', 'Items and Bosses'),
        ('Items Only', 'Items Only'),
        ('Bosses Only', 'Bosses Only')
    ]

    entity_choices = forms.ChoiceField(widget=forms.RadioSelect, choices=entity_choices, initial='Items and Bosses')
    wilderness = forms.ChoiceField(widget=forms.CheckboxInput, initial=True)
    slayer = forms.ChoiceField(widget=forms.CheckboxInput, initial=True)
    slayer_level = forms.IntegerField(min_value=0, max_value=99, initial=99)
    free_space = forms.ChoiceField(widget=forms.CheckboxInput, initial=True)
