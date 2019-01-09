from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from login.forms import SignUpForm


def home(request):
    print str(request.user.first_name)

    if request.user:
        context = {
            'display_name': request.user.first_name
        }
    else:
        context = {}

    return render(request, 'base.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=email, password=raw_password)

            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})
