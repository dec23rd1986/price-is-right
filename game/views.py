from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from accounts.views import signup
from .models import Game


def game_start(request):
    games = Game.objects.all().order_by('date')
    response = signup(request)
    if response['user_created']: #if user is created we are directing them to game 1
        return render (request, 'retailPrice/retailPrice_start.html')
    else: #else we are redirecting them back to homepage for now
        return render(request, 'game/game_start.html', {
                'games':games,
                'form': response['form'],
    })
