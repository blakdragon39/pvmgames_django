from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from games.models import Competition
from login.forms import SignUpForm


def home(request):
    context = {}

    all_competitions = Competition.objects.all()

    if request.user.is_authenticated():
        your_competitions = Competition.objects.filter(user=request.user)
        context['your_competitions'] = your_competitions
        context['all_competitions'] = all_competitions.exclude(id__in=your_competitions) if your_competitions else all_competitions
    else:
        context['all_competitions'] = all_competitions

    return render(request, 'home.html', context)


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


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=email, password=raw_password)

            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})
