from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import EmailField, forms


class SignUpForm(UserCreationForm):
    email = EmailField(label='Email address',
                       required=True,
                       help_text='Required.')

    class Meta:
        model = User
        fields = ('email', 'first_name', 'password1', 'password2')

    def clean_first_name(self):
        display_name = self.cleaned_data['first_name']
        if not display_name:
            raise forms.ValidationError('A display name is required', 'display_name_required')
        return display_name

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.username = self.cleaned_data['email']
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()

        return user
