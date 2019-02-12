from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from accounts.views import signup
from .models import Game


def game_start(request):
    games = Game.objects.all().order_by('date')
    data = {'msg': ''}
    response = signup(request)
    if response['user_created']: #if user is created we are directing them to game 1
        return render (request, 'retailPrice/retailPrice_start.html')
        data['msg'] = 'Thanks for being the part of our beautiful community!'
    else: #else we are redirecting them back to homepage for now
        return render(request, 'game/game_start.html', {
                'games':games,
                'form': response['form'],
                'msg': data['msg']
    })
